import os

# Get the tracer file path from the environment variable
tracer_file = os.getenv('TRACER_FILE', '/default-tracer-file-path/')

# Extract the base filename (without extension) to use as handle
handle = os.path.splitext(os.path.basename(tracer_file))[0]

# Determine the output folder based on the tracer file path
if 'gevolution' in tracer_file:
    output_folder_base = '/mnt/ssd-ext/gevolution-phi/revolver-outputs/'
elif 'screening' in tracer_file:
    output_folder_base = '/mnt/ssd-ext/screening-phi/revolver-outputs/'
else:
    output_folder_base = '/default-output-folder-path/'  # Default if neither gevolution nor screening is found

# Extract the last folder from the tracer file path to append to the output folder
output_subdir = os.path.basename(os.path.dirname(tracer_file))

# Ensure the output folder ends with a trailing '/'
output_folder = os.path.join(output_folder_base, output_subdir) + '/'

# Remaining parameters
tracer_file_type = 2
do_recon = False
is_box = True
box_length = 320.
zobov_buffer = 0.15  
void_prefix = 'voids_halo_' + handle.split('_')[-1]
verbose = True
use_barycentres = True
run_voxelvoids = False
do_tessellation = True
zobov_box_div = 2

# Optionally, print or log for confirmation
if verbose:
    print(f"Tracer file: {tracer_file}")
    print(f"Handle: {handle}")
    print(f"Output folder: {output_folder}")