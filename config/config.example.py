from __future__ import annotations

# ============================================================================
# 配置模板 —— 复制为 config/config.py 后再填写真实值
#
#   Windows : copy config\config.example.py config\config.py
#   Linux   : cp config/config.example.py config/config.py
#
# config/config.py 已被 .gitignore 排除，真实 token / API Key 只放在本地，
# 不要提交到仓库。使用 AstrBot 插件的「一键部署（auto 模式）」时，
# 插件会根据插件面板里的配置自动重写 config/config.py，无需手工维护。
# ============================================================================

# ======================= Core Service ====================== #
API_HOST = '127.0.0.1'
API_PORT = 18081
USE_STREAM_RESPONSE = True
ENABLE_DATABASE_WRITE = True

# ======================= 渲染开关 ========================== #
# 在使用大神数据或素材的渲染图片底部显示战绩查询宣传横幅。True 显示，False 不显示。
SHOW_DASHEN_PROMO = False
# 英雄热力图数据源：0（或省略）= 大神，1 = 微信小程序。
# 小程序请求通过 POST body 携带 xcxtoken，不要写在这里。
HERO_MODULE_MODE = 0

# ======================= Dashen Upstream =================== #
# 至少配置一个网易大神账号。上游（Overstats）本身支持账号池轮询：
# 配置多个账号后请求会在池内分摊，跨海查询吞吐随之提高，无需额外代码改动。
# 账号越多，下面两个并发参数才可以按「≤ 账号数 × 4」相应上调。
DASHEN_ACCOUNTS = [
    {
        'name': 'account-1',
        'role_id': 123456789,
        'token': 'replace-with-your-token',
    },
    # 有第二个账号时取消注释即可参与轮询：
    # {
    #     'name': 'account-2',
    #     'role_id': 987654321,
    #     'token': 'replace-with-your-token',
    # },
]

DASHEN_DTS = 2026
DASHEN_SERVER = 1

# 单账号每秒请求上限（上游默认 5，单账号建议保持默认）
DASHEN_ACCOUNT_MAX_REQUESTS_PER_SECOND = 5
DASHEN_ACCOUNT_RATE_LIMIT_WINDOW_SECONDS = 1.0

DASHEN_CLIENT_TYPE = "60"
DASHEN_ORIGIN = "https://act.ds.163.com"
DASHEN_REFERER = "https://act.ds.163.com/"
DASHEN_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 "
    "app/df_client dfVersion/100111"
)

# 账号被上游限流 / 失效后的冷却秒数
DASHEN_ACCOUNT_FAILURE_COOLDOWN_SECONDS = 60

# 进程内全局并发请求上限（上游默认 2）
DASHEN_MAX_CONCURRENT_REQUESTS = 2
# 上游 v2 接口对「账号池大小 * 4」（排队 + 活跃）以上直接返回 429
DASHEN_MAX_ACCEPTED_REQUESTS = max(len(DASHEN_ACCOUNTS) * 4, 1)

# ---- 可选：代理 ----
# 查询国际服数据时使用的 HTTP 代理，留空表示不使用
DASHEN_INTERNATIONAL_PROXY = ''
# 网易接口代理列表，None 表示直连
DASHEN_NETEASE_PROXIES = [
    None,
]

# ======================= 赛事 / 素材 ======================= #
# OW 赛事 PandaScore API Key：https://app.pandascore.co/dashboard/main
OW_ESPORTS_API_KEY = ''

# 可选的外部 OW guess 素材目录（放在仓库目录之外，避免体积膨胀）
OW_GUESS_ASSET_ROOT = 'ow_guess_assets'

# ======================= Dashen Season ===================== #
# 自动取 max(DASHEN_CURRENT_SEASON, AIEvaluateConfig[*].seasonIdList)；
# 与插件面板 dashen_current_season 默认值保持一致；新赛季开启后两处一起改。
DASHEN_CURRENT_SEASON = 24
DASHEN_HISTORY_START_SEASON = 15

# ======================= OW Hero Leaderboard =============== #
OW_HERO_LEADERBOARD_CN_SEASON = 4

# ======================= Match Analysis ==================== #
# 兼容 OpenAI 协议的服务地址，例如：
#   https://api.deepseek.com/v1
#   https://api.openai.com/v1
# 也可以直接填写完整的 /chat/completions 地址。
ANALYSIS_BASE_URL = 'https://api.deepseek.com/v1'
ANALYSIS_API_KEY = 'replace-with-your-analysis-api-key'
ANALYSIS_PROXY = ''

ANALYSIS_OPENAI_MODEL = 'deepseek-flash'

# 可选：外部补丁说明 / 英雄维基抓取代理
PATCH_NOTES_USE_INTERNATIONAL_PROXY = False
PATCH_NOTES_INTERNATIONAL_PROXY = ''

# 只放人格 / 语气设定，任务指令与 JSON Schema 在 service.py 内维护
ANALYSIS_PERSONA_PROMPT = (
    '【核心原则】\n'
    '请保持绝对客观中立，拒绝阿谀奉承！不要因为查询指令的是焦点玩家就一味夸奖，'
    '如果焦点玩家表现平庸或拉垮请直接批评。\n\n'
    '【人格设定】\n'
    '你的说话人设是守望先锋的安燃。'
)
