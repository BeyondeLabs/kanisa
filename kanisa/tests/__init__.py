# flake8: noqa

from __future__ import absolute_import
from .banners import BannerTest
from .views.banners import (BannerManagementViewTest,
                            BannerPublicViewTest)
from .bible_passages import (BiblePassageBadInput,
                             BiblePassage,
                             ToPassageBadInput,
                             ToPassageGoodInput,
                             BiblePassageModelField)
from .diary import (DiaryTest,
                    DiaryGetWeekBoundsTest,
                    DiaryGetScheduleTest)
from .views.diary import (DiaryManagementViewTest,
                          DiaryPublicViewTest)
from .views.documents import DocumentManagementViewTest
from .kanisa_markup import KanisaMarkupTest
from .views.management import ManagementViewTest
from .navigation import NavigationElementTest
from .views.pages import (PageManagementViewTest,
                          PagePublicViewTest)
from .pages import (PageTest,
                    GetPageFromPathTest,
                    PageTemplatesTest)
from .views.public import PublicViewTest
from .sermons import SermonTest
from .views.sermons import (SermonManagementViewTest,
                            SermonPublicViewTest)
from .views.social import SocialViewTest
from .views.user import UserManagementViewTest
from .views.xhr import (XHRBiblePassageViewTest,
                        XHRUserPermissionViewTest,
                        XHRCreatePageViewTest,
                        XHRListPagesViewTest,
                        XHRMarkSermonSeriesComplete,
                        XHRScheduleRegularEventViewTest,
                        XHRFetchScheduleViewTest)
