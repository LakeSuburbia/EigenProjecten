

def golden_ratio(n):
    n += 1
    golden = 1.61803398874989484820458683436563811772030917980576286213544862270526046281890244970720720418939113748475408807538689175212663386222353693179318006076672635443338908659593958290563832266131992829026788067520876689250171169620703222104321626954862629631361443814975870122034080588795445474924618569536486444924104432077134494704956584678850987433944221254487706647809158846074998871240076521705751797883416625624940758906970400028121042762177111777805315317141011704666599146697987317613560067087480710131795236894275219484353056783002287856997829778347845878228911097625003026961561700250464338243776486102838312683303724292675263116533924731671112115881863851331620384005222165791286675294654906811317159934323597349498509040947621322298101726107059611645629909816290555208524790352406020172799747175342777592778625619432082750513121815628551222480939471234145170223735805772786160086883829523045926478780178899219902707769038953219681986151437803149974110692608867429622675756052317277752035361393621076738937645560606059216589466759551900400555908950229530942312482355212212415444006470340565734797663972394949946584578873039623090375033993856210242369025138680414577995698122445747178034173126453220416397232134044449487302315417676893752103068737880344170093954409627955898678723209512426893557309704509595684401755519881921802064052905518934947592600734852282101088194644544222318891319294689622002301443770269923007803085261180754519288770502109684249362713592518760777884665836150238913493333122310533923213624319263728910670503399282265263556209029798642472759772565508615487543574826471814145127000602389016207773224499435308899909501680328112194320481964387675863314798571911397815397807476150772211750826945863932045652098969855567814106968372884058746103378105444390943683583581381131168993855576975484149144534150912954070050194775486163075422641729394680367319805861833918328599130396072014455950449779212076124785645916160837059498786006970189409886400764436170933417270919143365013715766011480381430626238051432117348151005590134561011800790506381421527093085880928757034505078081454588199063361298279814117453392731208092897279222132980642946878242748740174505540677875708323731097591511776297844328474790817651809778726841611763250386121129143683437670235037111633072586988325871033632223810980901211019899176841491751233134015273384383723450093478604979294599158220125810459823092552872124137043614910205471855496118087642657651106054588147560443178479858453973128630162544876114852021706440411166076695059775783257039511087823082710647893902111569103927683845386333321565829659773103436032322545743637204124406408882673758433953679
    return round((golden**n-(-golden)**-n)/(2*golden-1))


def summation(n):
    fib = 1
    mem = 1
    mem2 = 0
    for i in range(n):
        fib = mem2 + fib
        mem2 = mem
        mem = fib
    return fib


for i in range(100):
    if summation(i) != golden_ratio(i):
        print(f"{i}   -   {summation(i)}   -   {golden_ratio(i)}")