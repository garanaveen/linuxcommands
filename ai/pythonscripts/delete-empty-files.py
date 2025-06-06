#!/usr/bin/env python3
"""
Script to recursively find and delete empty files in a directory tree.
Provides verbose output of all actions taken.
"""

import os
import sys
import argparse
from pathlib import Path


def delete_empty_files(root_path, dry_run=False):
    """
    Recursively walk through directories and delete empty files.

    Args:
        root_path (str): Root directory to start the search
        dry_run (bool): If True, only show what would be deleted without actually deleting

    Returns:
        tuple: (files_deleted, total_files_checked)
    """
    root_path = Path(root_path).resolve()
    files_deleted = 0
    total_files_checked = 0

    if not root_path.exists():
        print(f"Error: Path '{root_path}' does not exist!")
        return 0, 0

    if not root_path.is_dir():
        print(f"Error: Path '{root_path}' is not a directory!")
        return 0, 0

    print(f"Starting search in: {root_path}")
    print(f"Dry run mode: {'ON' if dry_run else 'OFF'}")
    print("-" * 60)

    try:
        # Walk through all directories and subdirectories
        for current_dir, dirs, files in os.walk(root_path):
            current_dir_path = Path(current_dir)

            # Skip hidden directories (optional)
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            print(f"Checking directory: {current_dir_path}")

            if not files:
                print(f"  No files in this directory")
                continue

            for filename in files:
                file_path = current_dir_path / filename
                total_files_checked += 1

                try:
                    # Check if file exists and get its size
                    if file_path.exists() and file_path.is_file():
                        file_size = file_path.stat().st_size

                        if file_size == 0:
                            print(f"  Found empty file: {file_path}")

                            if dry_run:
                                print(f"  [DRY RUN] Would delete: {file_path}")
                            else:
                                try:
                                    file_path.unlink()
                                    print(f"  ✓ Deleted: {file_path}")
                                    files_deleted += 1
                                except PermissionError:
                                    print(f"  ✗ Permission denied: {file_path}")
                                except OSError as e:
                                    print(f"  ✗ Error deleting {file_path}: {e}")
                        else:
                            print(f"  File has content ({file_size} bytes): {file_path.name}")

                except (OSError, PermissionError) as e:
                    print(f"  ✗ Error accessing {file_path}: {e}")

    except KeyboardInterrupt:
        print("\n\nOperation interrupted by user!")
        return files_deleted, total_files_checked

    return files_deleted, total_files_checked


def main():
    """Main function to handle command line arguments and execute the script."""
    parser = argparse.ArgumentParser(
        description="Recursively find and delete empty files in a directory tree",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python delete-empty-files.py /path/to/directory
  python delete-empty-files.py . --dry-run
  python delete-empty-files.py /home/user/documents
        """
    )

    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Root directory to search (default: current directory)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be deleted without actually deleting files'
    )

    args = parser.parse_args()

    print("=" * 60)
    print("EMPTY FILE DELETION SCRIPT")
    print("=" * 60)

    # Confirm action unless it's a dry run
    if not args.dry_run:
        response = input(f"Are you sure you want to delete empty files in '{args.path}'? (y/N): ")
        if response.lower() not in ['y', 'yes']:
            print("Operation cancelled.")
            return

    # Execute the deletion
    deleted_count, checked_count = delete_empty_files(args.path, args.dry_run)

    # Summary
    print("-" * 60)
    print("SUMMARY:")
    print(f"Total files checked: {checked_count}")
    print(f"Empty files found and {'would be ' if args.dry_run else ''}deleted: {deleted_count}")

    if args.dry_run and deleted_count > 0:
        print("\nTo actually delete the files, run the script without --dry-run flag.")


if __name__ == "__main__":
    main()