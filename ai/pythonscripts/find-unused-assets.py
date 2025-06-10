#!/usr/bin/env python3
"""
Find Unused Assets Script
=========================

This script helps maintain clean codebases by identifying unused asset files
(images, fonts, etc.) that are taking up space in your repository.

OVERVIEW:
---------
The script scans a specified assets directory for files with given extensions
(default: .png, .webp) and searches through your project's source code to
determine if each asset is referenced. Any unreferenced assets are reported
as "unused" and can be safely removed or marked as intentionally ignored.

PERFECT FOR CI/CD:
------------------
This script is designed to integrate seamlessly with CI/CD pipelines:
- Returns exit code 0 (success) when all assets are used
- Returns exit code 1 (failure) when unused assets are found
- Provides clear, actionable error messages for developers
- Supports ignore files for intentionally unused assets

USAGE EXAMPLES:
---------------

1. Basic usage - scan images directory:
   python3 find-unused-assets.py ecosystem/images

2. Scan with custom extensions:
   python3 find-unused-assets.py ecosystem/images --extensions .png .jpg .svg .webp

3. Use with ignore file:
   python3 find-unused-assets.py ecosystem/images --ignore-files .unused-assets-ignore

4. Verbose output showing where assets are used:
   python3 find-unused-assets.py ecosystem/images --verbose --show-used

5. Custom project root and exclude directories:
   python3 find-unused-assets.py assets --project-root /path/to/project --exclude-dirs build dist node_modules

IGNORE FILE FORMAT:
-------------------
Create a file (e.g., '.unused-assets-ignore') with asset filenames to ignore:

    # This is a comment - lines starting with # are ignored
    legacy-logo.png
    placeholder-image.webp
    backup-icon.png
    # Another comment
    old-banner.jpg

GITLAB CI/CD INTEGRATION:
-------------------------
Add this job to your .gitlab-ci.yml:

    check-unused-assets:
      stage: test
      image: python:3.9-slim
      script:
        - python3 scripts/find-unused-assets.py ecosystem/images --ignore-files .unused-assets-ignore
      rules:
        - if: $CI_PIPELINE_SOURCE == "merge_request_event"
        - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
      allow_failure: false

GITHUB ACTIONS INTEGRATION:
---------------------------
Add this to your .github/workflows/ci.yml:

    - name: Check for unused assets
      run: |
        python3 scripts/find-unused-assets.py ecosystem/images --ignore-files .unused-assets-ignore

JENKINS INTEGRATION:
--------------------
Add this to your Jenkinsfile:

    stage('Check Unused Assets') {
        steps {
            sh 'python3 scripts/find-unused-assets.py ecosystem/images --ignore-files .unused-assets-ignore'
        }
    }

SUPPORTED FILE TYPES:
---------------------
By default, the script searches these file types for asset references:
- Source code: .brs, .js, .ts, .jsx, .tsx, .py, .sh, .bat
- Markup: .xml, .html, .htm
- Stylesheets: .css, .scss, .sass, .less
- Config files: .json, .yaml, .yml, .cfg, .config, .properties
- Documentation: .md, .txt
- Build files: .mk, .makefile, Makefile, Dockerfile

SEARCH PATTERNS:
----------------
The script searches for assets using multiple patterns:
- Full relative path: images/icons/logo.png
- Filename only: logo.png
- Cross-platform paths: images\\icons\\logo.png (Windows) and images/icons/logo.png (Unix)
- Framework-specific patterns: pkg:/images/icons/logo.png (Roku apps)

EXIT CODES:
-----------
- 0: Success - No unused assets found
- 1: Failure - Unused assets detected (triggers CI/CD failure)

TROUBLESHOOTING:
----------------
If an asset is marked as unused but you know it's used:
1. Check if it's dynamically referenced (string concatenation, variables)
2. Add it to an ignore file
3. Use --verbose to see what patterns are being searched
4. Verify the asset path is correct relative to project root
"""

import os
import sys
import argparse
import re
from pathlib import Path
from typing import Set, List, Tuple


def load_ignore_list(ignore_file_path: str) -> Set[str]:
    """
    Load list of asset names to ignore from a file.

    Args:
        ignore_file_path: Path to the file containing asset names to ignore

    Returns:
        Set of asset names to ignore
    """
    ignore_set = set()

    if not ignore_file_path:
        return ignore_set

    try:
        with open(ignore_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Strip whitespace and skip empty lines and comments
                asset_name = line.strip()
                if asset_name and not asset_name.startswith('#'):
                    ignore_set.add(asset_name)

        print(f"Loaded {len(ignore_set)} assets to ignore from {ignore_file_path}")

    except (IOError, OSError) as e:
        print(f"Warning: Could not read ignore file {ignore_file_path}: {e}", file=sys.stderr)

    return ignore_set


def find_asset_files(assets_dir: str, extensions: List[str] = ['.png', '.webp']) -> List[str]:
    """
    Find all asset files with specified extensions in the given directory.

    Args:
        assets_dir: Directory to search for assets
        extensions: List of file extensions to search for

    Returns:
        List of asset file paths
    """
    asset_files = []

    for root, dirs, files in os.walk(assets_dir):
        for file in files:
            if any(file.lower().endswith(ext.lower()) for ext in extensions):
                asset_files.append(os.path.join(root, file))

    return asset_files


def get_project_files(project_root: str, exclude_dirs: Set[str] = None) -> List[str]:
    """
    Get all text files in the project that could contain asset references.

    Args:
        project_root: Root directory of the project
        exclude_dirs: Set of directory names to exclude from search

    Returns:
        List of project file paths
    """
    if exclude_dirs is None:
        exclude_dirs = {
            '.git', '.svn', 'node_modules', '__pycache__', '.pytest_cache',
            'build', 'dist', '.vscode', '.idea', 'out', 'bin', 'obj'
        }

    # File extensions that typically contain asset references
    text_extensions = {
        '.brs', '.xml', '.js', '.ts', '.jsx', '.tsx', '.html', '.htm',
        '.css', '.scss', '.sass', '.less', '.json', '.yaml', '.yml',
        '.md', '.txt', '.cfg', '.config', '.properties', '.manifest',
        '.mk', '.makefile', '.py', '.sh', '.bat', '.cmd'
    }

    project_files = []

    for root, dirs, files in os.walk(project_root):
        # Remove excluded directories from dirs list to avoid walking into them
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)

            # Include files with text extensions or common config files without extensions
            if (ext.lower() in text_extensions or
                file.lower() in ['makefile', 'dockerfile', 'readme']):
                project_files.append(file_path)

    return project_files


def search_asset_references(asset_path: str, project_files: List[str], project_root: str) -> List[Tuple[str, int, str]]:
    """
    Search for references to an asset file in the project files.

    Args:
        asset_path: Path to the asset file
        project_files: List of project files to search in
        project_root: Root directory of the project

    Returns:
        List of tuples (file_path, line_number, line_content) where references are found
    """
    references = []

    # Get relative path from project root
    try:
        rel_asset_path = os.path.relpath(asset_path, project_root)
    except ValueError:
        # If asset_path is not under project_root, use the full path
        rel_asset_path = asset_path

    # Get just the filename
    asset_filename = os.path.basename(asset_path)

    # Create search patterns
    patterns = [
        re.escape(rel_asset_path),  # Full relative path
        re.escape(asset_filename),  # Just filename
        re.escape(rel_asset_path.replace('\\', '/')),  # Unix-style path
        re.escape(rel_asset_path.replace('/', '\\')),  # Windows-style path
    ]

    # Add patterns with pkg:/ prefix (common in Roku apps)
    if 'images/' in rel_asset_path:
        pkg_path = 'pkg:/' + rel_asset_path.replace('\\', '/')
        patterns.append(re.escape(pkg_path))

    # Remove duplicates
    patterns = list(set(patterns))

    for file_path in project_files:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    line_lower = line.lower()

                    # Check each pattern
                    for pattern in patterns:
                        if re.search(pattern, line, re.IGNORECASE):
                            references.append((file_path, line_num, line.strip()))
                            break  # Found a match, no need to check other patterns for this line

        except (IOError, OSError) as e:
            print(f"Warning: Could not read file {file_path}: {e}", file=sys.stderr)
            continue

    return references


def main():
    parser = argparse.ArgumentParser(
        description='Find unused assets in a project and report them for cleanup',
        epilog='''
Examples:
  %(prog)s ecosystem/images
  %(prog)s assets --extensions .png .jpg .svg
  %(prog)s images --ignore-files .unused-assets-ignore --verbose

Exit codes:
  0 - Success: No unused assets found
  1 - Failure: Unused assets detected (CI/CD will fail)
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('assets_dir', help='Directory containing assets to check')
    parser.add_argument('--project-root', default='.',
                       help='Root directory of the project (default: current directory)')
    parser.add_argument('--extensions', nargs='+', default=['.png', '.webp'],
                       help='Asset file extensions to search for (default: .png .webp)')
    parser.add_argument('--exclude-dirs', nargs='+',
                       default=['.git', '.svn', 'node_modules', '__pycache__', 'build', 'dist'],
                       help='Directories to exclude from search')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Show detailed information including where assets are used')
    parser.add_argument('--show-used', action='store_true',
                       help='Also show assets that are being used')
    parser.add_argument('--ignore-files', help='File containing list of asset names to ignore')

    args = parser.parse_args()

    # Validate directories
    if not os.path.isdir(args.assets_dir):
        print(f"Error: Assets directory '{args.assets_dir}' does not exist", file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(args.project_root):
        print(f"Error: Project root '{args.project_root}' does not exist", file=sys.stderr)
        sys.exit(1)

    # Convert to absolute paths
    assets_dir = os.path.abspath(args.assets_dir)
    project_root = os.path.abspath(args.project_root)

    print(f"Searching for unused assets...")
    print(f"Assets directory: {assets_dir}")
    print(f"Project root: {project_root}")
    print(f"Extensions: {', '.join(args.extensions)}")
    print("-" * 60)

    # Load ignore list
    ignore_set = load_ignore_list(args.ignore_files)

    # Find all asset files
    asset_files = find_asset_files(assets_dir, args.extensions)
    print(f"Found {len(asset_files)} asset files")

    # Get all project files
    exclude_dirs = set(args.exclude_dirs)
    project_files = get_project_files(project_root, exclude_dirs)
    print(f"Searching in {len(project_files)} project files")
    print("-" * 60)

    unused_assets = []
    used_assets = []

    for i, asset_path in enumerate(asset_files, 1):
        if args.verbose:
            print(f"Checking asset {i}/{len(asset_files)}: {os.path.relpath(asset_path, project_root)}")

        # Skip assets in the ignore list
        if os.path.basename(asset_path) in ignore_set:
            if args.verbose:
                print(f"  ➔ Ignored (in ignore list)")
            continue

        references = search_asset_references(asset_path, project_files, project_root)

        if references:
            used_assets.append((asset_path, references))
            if args.verbose:
                print(f"  ✓ Found {len(references)} reference(s)")
        else:
            unused_assets.append(asset_path)
            if args.verbose:
                print(f"  ✗ No references found")

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)

    if unused_assets:
        print(f"\n❌ ERROR: Found {len(unused_assets)} unused asset(s):")
        print("-" * 60)
        for asset in unused_assets:
            rel_path = os.path.relpath(asset, project_root)
            print(f"  • {rel_path}")

        print("\n" + "⚠️  " + "=" * 58)
        print("CI/CD PIPELINE FAILURE")
        print("=" * 60)
        print("This pipeline has failed because unused assets were detected.")
        print("These assets are taking up space and should be removed or marked as ignored.")
        print("\nTo resolve this issue, you have two options:")
        print("\n1. DELETE the unused assets listed above from your repository")
        print("\n2. CREATE an ignore file if these assets are intentionally unused:")
        print("   • Create a file (e.g., '.unused-assets-ignore') containing asset names to ignore")
        print("   • Add one asset filename per line (just the filename, not the full path)")
        print("   • Lines starting with '#' are treated as comments")
        print("   • Example ignore file content:")
        print("     # This is a comment")
        print("     legacy-logo.png")
        print("     placeholder-image.webp")
        print("     # Another comment")
        print("     backup-icon.png")
        print("   • Then run this script with: --ignore-files path/to/your/ignore/file")
        print("\n" + "=" * 60)
    else:
        print("\n✅ SUCCESS: No unused assets found!")
        print("All assets in the specified directory are being used in the codebase.")

    if args.show_used and used_assets:
        print(f"\n📋 USED ASSETS ({len(used_assets)}):")
        print("-" * 40)
        for asset_path, references in used_assets:
            rel_path = os.path.relpath(asset_path, project_root)
            print(f"  • {rel_path} ({len(references)} reference(s))")

            if args.verbose:
                for ref_file, line_num, line_content in references[:3]:  # Show first 3 references
                    ref_rel_path = os.path.relpath(ref_file, project_root)
                    print(f"    └─ {ref_rel_path}:{line_num} - {line_content[:80]}...")
                if len(references) > 3:
                    print(f"    └─ ... and {len(references) - 3} more reference(s)")

    print(f"\n📊 SUMMARY:")
    print(f"  • Total assets scanned: {len(asset_files)}")
    print(f"  • Assets in use: {len(used_assets)}")
    print(f"  • Unused assets: {len(unused_assets)}")
    if ignore_set:
        print(f"  • Assets ignored: {len(ignore_set)}")

    # Exit with non-zero code if unused assets found (CI/CD failure)
    if unused_assets:
        print(f"\n🚨 CI/CD Pipeline Status: FAILED (exit code 1)")
        print(f"   Reason: {len(unused_assets)} unused asset(s) detected")
        sys.exit(1)
    else:
        print(f"\n✅ CI/CD Pipeline Status: PASSED (exit code 0)")
        sys.exit(0)


if __name__ == '__main__':
    main()
