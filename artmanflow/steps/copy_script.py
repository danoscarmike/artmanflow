import subprocess

staging_path = '/usr/local/google/home/vam/_/projects/github/vam-google/api-client-staging/generated/java'
dest_path = '/usr/local/google/home/vam/_/projects/github/vam-google/google-cloud-java'

mapping = {
    'gapic-google-cloud-bigquerydatatransfer-v1': 'google-cloud-bigquerydatatransfer',
    'gapic-google-cloud-bigtable-v2': 'google-cloud-bigtable',
    'gapic-google-cloud-bigtable-admin-v2': 'google-cloud-bigtable',
    'gapic-google-cloud-container-v1': 'google-cloud-container',
    'gapic-google-cloud-dataproc-v1': 'google-cloud-dataproc',
    'gapic-google-cloud-dialogflow-v2beta1': 'google-cloud-dialogflow',
    'gapic-google-cloud-dialogflow-v2': 'google-cloud-dialogflow',
    'gapic-google-cloud-dlp-v2beta1': 'google-cloud-dlp',
    # 'gapic-google-cloud-dlp-v2beta2': 'google-cloud-dlp',
    'gapic-google-cloud-dlp-v2': 'google-cloud-dlp',
    'gapic-google-cloud-error-reporting-v1beta1': 'google-cloud-errorreporting',
    'gapic-google-cloud-firestore-v1beta1': 'google-cloud-firestore',
    'gapic-google-cloud-language-v1': 'google-cloud-language',
    'gapic-google-cloud-language-v1beta2': 'google-cloud-language',
    'gapic-google-cloud-logging-v2': 'google-cloud-logging',
    'gapic-google-cloud-os-login-v1': 'google-cloud-os-login',
    'gapic-google-cloud-monitoring-v3': 'google-cloud-monitoring',
    'gapic-google-cloud-pubsub-v1': 'google-cloud-pubsub',
    'gapic-google-cloud-speech-v1': 'google-cloud-speech',
    'gapic-google-cloud-speech-v1beta1': 'google-cloud-speech',
    'gapic-google-cloud-speech-v1p1beta1': 'google-cloud-speech',
    'gapic-google-cloud-texttospeech-v1beta1': 'google-cloud-texttospeech',
    'gapic-google-cloud-trace-v1': 'google-cloud-trace',
    'gapic-google-cloud-trace-v2': 'google-cloud-trace',
    'gapic-google-cloud-video-intelligence-v1beta1': 'google-cloud-video-intelligence',
    'gapic-google-cloud-video-intelligence-v1beta2': 'google-cloud-video-intelligence',
    'gapic-google-cloud-video-intelligence-v1p1beta1': 'google-cloud-video-intelligence',
    'gapic-google-cloud-video-intelligence-v1': 'google-cloud-video-intelligence',
    'gapic-google-cloud-vision-v1': 'google-cloud-vision',
    'gapic-google-cloud-vision-v1p1beta1': 'google-cloud-vision',
    'gapic-google-cloud-vision-v1p2beta1': 'google-cloud-vision'
}

for src_name, dest_name in mapping.items():
    cmd = "cp -r %s/%s/src %s/%s" % (staging_path, src_name, dest_path, dest_name)
    print(cmd)
    subprocess.call(cmd.split())