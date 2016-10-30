
# It's a configuration file, you can change this variables if you want get addition fields

# BY USING FUNCTION helpClasses/gitFaceUtils.py/filter_keys()


# ================ PROFILE

__profile_required_keys = ('login', 'name', 'html_url', 'avatar_url', 'bio', 'email', 'location', 'created_at', 'company', 'blog', 'followers', 'public_repos',)

# ('following_url', 'https://api.github.com/users/mbostock/following{/other_user}')
# ('events_url', 'https://api.github.com/users/mbostock/events{/privacy}')
# ('followers', 13599)
# ('url', 'https://api.github.com/users/mbostock')
# ('avatar_url', 'https://avatars.githubusercontent.com/u/230541?v=3')
# ('received_events_url', 'https://api.github.com/users/mbostock/received_events')
# ('organizations_url', 'https://api.github.com/users/mbostock/orgs')
# ('starred_url', 'https://api.github.com/users/mbostock/starred{/owner}{/repo}')
# ('html_url', 'https://github.com/mbostock')
# ('email', 'mike@ocks.org')
# ('followers_url', 'https://api.github.com/users/mbostock/followers')
# ('gists_url', 'https://api.github.com/users/mbostock/gists{/gist_id}')
# ('hireable', None)
# ('following', 13)
# ('bio', 'I design tools for humans. Creator of @d3. Former @nytgraphics editor.')
# ('gravatar_id', '')
# ('created_at', '2010-03-25T22:02:56Z')
# ('type', 'User')
# ('repos_url', 'https://api.github.com/users/mbostock/repos')
# ('public_repos', 53)
# ('company', None)
# ('updated_at', '2016-10-23T23:14:32Z')
# ('site_admin', False)
# ('id', 230541)
# ('blog', 'http://bost.ocks.org')
# ('login', 'mbostock')
# ('subscriptions_url', 'https://api.github.com/users/mbostock/subscriptions')
# ('name', 'Mike Bostock')
# ('public_gists', 987)
# ('location', 'San Francisco, CA')

#  + 'organisations' field with list of organisations
# 'organisations', [{'login': 'protovis', 'avatar_url': 'https://avatars.githubusercontent.com/u/430480?v=3', 'html_url': 'https://github.com/protovis'}, {'login': 'd3', 'avatar_url': 'https://avatars.githubusercontent.com/u/1562726?v=3', 'html_url': 'https://github.com/d3'}])
# ('followers', 13599)

# to see how 'organisations' field is build look into helpClasses/api_services.py/get_profile_dict() function


# =========== ORGANISATION

__organisation_required_keys = ('login', 'avatar_url', 'html_url')

# ('repos_url', 'https://api.github.com/orgs/protovis/repos')
# ('updated_at', '2015-05-31T16:22:40Z')
# ('login', 'protovis')
# ('public_gists', 0)
# ('type', 'Organization')
# ('public_repos', 3)
# ('blog', 'http://protovis.org')
# ('issues_url', 'https://api.github.com/orgs/protovis/issues')
# ('id', 430480)
# ('url', 'https://api.github.com/orgs/protovis')
# ('email', '')
# ('avatar_url', 'https://avatars.githubusercontent.com/u/430480?v=3')
# ('description', '')
# ('public_members_url', 'https://api.github.com/orgs/protovis/public_members{/member}')
# ('name', 'Protovis')
# ('following', 0)
# ('company', None)
# ('members_url', 'https://api.github.com/orgs/protovis/members{/member}')
# ('location', 'Stanford, CA')
# ('hooks_url', 'https://api.github.com/orgs/protovis/hooks')
# ('html_url', 'https://github.com/protovis')
# ('events_url', 'https://api.github.com/orgs/protovis/events')
# ('followers', 0)
# ('created_at', '2010-10-07T03:46:54Z')


# To protect this configuration from runtime vulnerability
class __RequiredFields(object):
    def __init__(self, profile_required_keys, organisation_required_keys):
        self._profile_required_keys = profile_required_keys
        self._organisation_required_keys = organisation_required_keys

    @property
    def profile_required_keys(self):
        return self._profile_required_keys

    @property
    def organisation_required_keys(self):
        return self._organisation_required_keys


# Config Instance
ConfInstance = __RequiredFields(profile_required_keys=__profile_required_keys,
                                organisation_required_keys=__organisation_required_keys)
