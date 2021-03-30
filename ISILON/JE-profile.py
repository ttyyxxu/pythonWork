import re

LOW_profile = '''impact.profiles.low.id (enum job_impact_id) = Low
impact.profiles.low.ionice (int) = 3
impact.profiles.low.workers_per_core (float) = 0.25
impact.profiles.low.min_workers_per_cluster (float) = 0.25
impact.profiles.low.max_workers_per_storage_unit (float) = 0.5
impact.profiles.low.fixed_worker_count (float) = 0
impact.profiles.low.max_node_load_factor (float) = 2
impact.profiles.low.min_node_load_factor (float) = 1
impact.profiles.low.disk_types.sata.type (enum disk_type) = sata
impact.profiles.low.disk_types.sata.enabled (bool) = true
impact.profiles.low.disk_types.sata.max_client_load_kbps (int) = 1024
impact.profiles.low.disk_types.sata.max_disk_iosched_qsize_under_load (int) = 40
impact.profiles.low.disk_types.sata.max_disk_iosched_qsize (int) = 80
impact.profiles.low.disk_types.sata.max_je_load_kbps (int) = 5000
impact.profiles.low.disk_types.sata.min_je_load_kbps (int) = 2000
impact.profiles.low.disk_types.sata.max_je_load_iops (int) = 500
impact.profiles.low.disk_types.sata.min_je_load_iops (int) = 100
impact.profiles.low.disk_types.sas.type (enum disk_type) = sas
impact.profiles.low.disk_types.sas.enabled (bool) = true
impact.profiles.low.disk_types.sas.max_client_load_kbps (int) = 1024
impact.profiles.low.disk_types.sas.max_disk_iosched_qsize_under_load (int) = 40
impact.profiles.low.disk_types.sas.max_disk_iosched_qsize (int) = 80
impact.profiles.low.disk_types.sas.max_je_load_kbps (int) = 6000
impact.profiles.low.disk_types.sas.min_je_load_kbps (int) = 2000
impact.profiles.low.disk_types.sas.max_je_load_iops (int) = 600
impact.profiles.low.disk_types.sas.min_je_load_iops (int) = 120
impact.profiles.low.thread_decrease_amount (float) = 0.2
impact.profiles.low.thread_increase_amount (float) = 0.1'''

MEDIUM_profile = '''impact.profiles.medium.id (enum job_impact_id) = Medium
impact.profiles.medium.ionice (int) = 1
impact.profiles.medium.workers_per_core (float) = 0
impact.profiles.medium.min_workers_per_cluster (float) = 0.25
impact.profiles.medium.max_workers_per_storage_unit (float) = 2
impact.profiles.medium.fixed_worker_count (float) = 0
impact.profiles.medium.max_node_load_factor (float) = 3
impact.profiles.medium.min_node_load_factor (float) = 2
impact.profiles.medium.disk_types.sata.type (enum disk_type) = sata
impact.profiles.medium.disk_types.sata.enabled (bool) = true
impact.profiles.medium.disk_types.sata.max_client_load_kbps (int) = 1024
impact.profiles.medium.disk_types.sata.max_disk_iosched_qsize_under_load (int) = 80
impact.profiles.medium.disk_types.sata.max_disk_iosched_qsize (int) = 120
impact.profiles.medium.disk_types.sata.max_je_load_kbps (int) = 6000
impact.profiles.medium.disk_types.sata.min_je_load_kbps (int) = 3000
impact.profiles.medium.disk_types.sata.max_je_load_iops (int) = 1000
impact.profiles.medium.disk_types.sata.min_je_load_iops (int) = 150
impact.profiles.medium.disk_types.sas.type (enum disk_type) = sas
impact.profiles.medium.disk_types.sas.enabled (bool) = true
impact.profiles.medium.disk_types.sas.max_client_load_kbps (int) = 1024
impact.profiles.medium.disk_types.sas.max_disk_iosched_qsize_under_load (int) = 80
impact.profiles.medium.disk_types.sas.max_disk_iosched_qsize (int) = 120
impact.profiles.medium.disk_types.sas.max_je_load_kbps (int) = 7000
impact.profiles.medium.disk_types.sas.min_je_load_kbps (int) = 3000
impact.profiles.medium.disk_types.sas.max_je_load_iops (int) = 1200
impact.profiles.medium.disk_types.sas.min_je_load_iops (int) = 180
impact.profiles.medium.thread_decrease_amount (float) = 0.5
impact.profiles.medium.thread_increase_amount (float) = 0.5'''

HIGH_profile='''impact.profiles.high.id (enum job_impact_id) = High
impact.profiles.high.ionice (int) = 0
impact.profiles.high.workers_per_core (float) = 2
impact.profiles.high.min_workers_per_cluster (float) = 0.25
impact.profiles.high.max_workers_per_storage_unit (float) = 8
impact.profiles.high.fixed_worker_count (float) = 0
impact.profiles.high.max_node_load_factor (float) = 4
impact.profiles.high.min_node_load_factor (float) = 3
impact.profiles.high.disk_types.sata.type (enum disk_type) = sata
impact.profiles.high.disk_types.sata.enabled (bool) = true
impact.profiles.high.disk_types.sata.max_client_load_kbps (int) = 2048
impact.profiles.high.disk_types.sata.max_disk_iosched_qsize_under_load (int) = 100
impact.profiles.high.disk_types.sata.max_disk_iosched_qsize (int) = 200
impact.profiles.high.disk_types.sata.max_je_load_kbps (int) = 7000
impact.profiles.high.disk_types.sata.min_je_load_kbps (int) = 3000
impact.profiles.high.disk_types.sata.max_je_load_iops (int) = 2000
impact.profiles.high.disk_types.sata.min_je_load_iops (int) = 250
impact.profiles.high.disk_types.sas.type (enum disk_type) = sas
impact.profiles.high.disk_types.sas.enabled (bool) = true
impact.profiles.high.disk_types.sas.max_client_load_kbps (int) = 2048
impact.profiles.high.disk_types.sas.max_disk_iosched_qsize_under_load (int) = 100
impact.profiles.high.disk_types.sas.max_disk_iosched_qsize (int) = 200
impact.profiles.high.disk_types.sas.max_je_load_kbps (int) = 8000
impact.profiles.high.disk_types.sas.min_je_load_kbps (int) = 3000
impact.profiles.high.disk_types.sas.max_je_load_iops (int) = 2400
impact.profiles.high.disk_types.sas.min_je_load_iops (int) = 300
impact.profiles.high.thread_decrease_amount (float) = 0.9
impact.profiles.high.thread_increase_amount (float) = 0.8'''

high_dict = {x.split()[0]:x.split()[-1] for x in HIGH_profile.split('\n')}

medium_dict = {x.split()[0]:x.split()[-1] for x in MEDIUM_profile.split('\n')}

low_dict = {x.split()[0]:x.split()[-1] for x in LOW_profile.split('\n')}

# for h_key in high_dict:
#     m_key = h_key.replace('high','medium')
#     print("isi_gconfig -t job-config ",h_key,"=",medium_dict[m_key],sep='')

# for m_key in medium_dict:
#     l_key = m_key.replace('medium','low')
#     print("isi_gconfig -t job-config ",m_key,"=",low_dict[l_key],sep='')


## To revert back ##
# for h_key in high_dict:
#     print("isi_gconfig -t job-config ",h_key,"=",high_dict[h_key],sep='')

# for m_key in medium_dict:
#     print("isi_gconfig -t job-config ",m_key,"=",medium_dict[m_key],sep='')

for l_key in low_dict:
    print("isi_gconfig -t job-config ",l_key,"=",low_dict[l_key],sep='')