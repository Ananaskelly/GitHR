from gitFace.helpClasses.gitFaceUtils import filter_keys
from gitFace.configurations.api_fields import ConfInstance


"""
params :
    git_conn = github.Github(token)
    profile_name = 'user_name'
    profile_required_keys, organisation_required_keys
"""
def get_profile_dict(
        git_conn,
        profile_name=None,
        profile_required_keys=ConfInstance.profile_required_keys,
        organisation_required_keys=ConfInstance.organisation_required_keys
):

    # print("=============================here")
    user = git_conn.get_user() if profile_name is None else git_conn.get_user(profile_name)
    data = user.raw_data

    res_data = filter_keys(data, profile_required_keys)

    res_data['repos_url'] = res_data['html_url'] + '?tab=repositories'

    if not profile_name is None:
        res_data['organisations'] = [filter_keys(org.raw_data, organisation_required_keys) for org in user.get_orgs()]

    # print(res_data)
    return res_data
