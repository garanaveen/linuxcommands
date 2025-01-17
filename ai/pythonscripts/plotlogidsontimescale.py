import re
import argparse
import matplotlib.pyplot as plt
from datetime import datetime

def parse_logs(file_path, log_id):
    logs = []
    pattern = re.compile(r"(\d{2}:\d{2}:\d{2}\.\d{3}) \*\[" + re.escape(log_id) + r"\] DisplayNextCamera\(\) - .*")
    
    with open(file_path, "r") as file:
        for line in file:
            match = pattern.search(line)
            if match:
                timestamp = match.group(1)
                logs.append(timestamp)
    return logs

def plot_logs(timestamps):
    # Convert timestamps to datetime objects
    times = [datetime.strptime(ts, "%H:%M:%S.%f") for ts in timestamps]
    differences = [(times[i] - times[i-1]).total_seconds() for i in range(1, len(times))]
    
    # Create a proportional spacing for the graph
    x_positions = [0]
    for diff in differences:
        x_positions.append(x_positions[-1] + diff)
    
    # Plot the logs
    plt.figure(figsize=(10, 4))
    plt.scatter(x_positions, [1]*len(x_positions), color="blue", s=100, label="Log Entries")
    
    # Add annotations and emphasis
    for i, ts in enumerate(timestamps):
        plt.annotate(
            ts, 
            (x_positions[i], 1), 
            textcoords="offset points", 
            xytext=(0, 10), 
            ha="center", 
            rotation=90,  # Rotate the text vertically
            fontsize=9    # Adjust font size if needed
        )
        if i > 0 and (times[i] - times[i-1]).total_seconds() <= 2:
            plt.plot(x_positions[i-1:i+1], [1, 1], color="red", linewidth=2, label="Close Logs" if i == 1 else None)
    
    plt.title("Log Timestamps Visualization")
    plt.xlabel("Time Progression (Proportional)")
    plt.yticks([])
    plt.legend(loc="upper right")
    plt.grid(True, axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Filter logs and plot time-based visualization.")
    parser.add_argument("--file", required=True, help="Path to the log file.")
    parser.add_argument("--logid", required=True, help="Log ID to filter.")
    args = parser.parse_args()
    
    timestamps = parse_logs(args.file, args.logid)
    if timestamps:
        plot_logs(timestamps)
    else:
        print(f"No logs found with Log ID: {args.logid}")

if __name__ == "__main__":
    main()

