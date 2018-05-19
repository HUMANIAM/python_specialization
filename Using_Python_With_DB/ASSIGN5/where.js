myData = [
[30.0444196,31.2357116, 'Cairo, Cairo Governorate, Egypt'],
[41.8918552,-87.6320197, '118 W Grand Ave, Chicago, IL 60654, USA'],
[30.7066802,31.2447709, 'Zifta, Madinet Zefta, Zefta, Gharbia Governorate, Egypt'],
[50.06688579999999,19.9136192, 'aleja Adama Mickiewicza 30, 30-059 Kraków, Poland'],
[52.2394019,21.0150792, 'Krakowskie Przedmieście 5, 00-068 Warszawa, Poland'],
[40.750808,-73.9832916, '420 5th Ave, New York, NY 10018, USA'],
[33.4242399,-111.9280527, 'Tempe, AZ 85281, USA'],
[38.0399391,23.8030901, 'Monumental Plaza, Building C, 1st Floor, Leof. Kifisias 44, Marousi 151 25, Greece'],
[28.3639976,75.58696809999999, 'VidyaVihar Campus, Pilani, Rajasthan 333031, India'],
[6.8919631,3.7186605, 'Ilishan Remo Ogun State Nigeria, ILISHAN REMO, Nigeria'],
[25.2677203,82.99125819999999, 'Ajagara, Banaras Hindu University Campus, Varanasi, Uttar Pradesh 221005, India'],
[12.9527314,77.5157387, 'Gnana Bharathi Main road, Bengaluru, Karnataka 560056, India'],
[31.549841,-97.1143146, '1301 S University Parks Dr, Waco, TX 76706, USA'],
[39.9619537,116.3662615, '19 Xinjiekou Outer St, BeiTaiPingZhuang, Haidian Qu, Beijing Shi, China, 100875'],
[53.8930389,27.5455567, 'Prospekt Nezavisimosti 4, Minsk, Belarus'],
[44.8184339,20.4575676, 'Studentski trg 1, Beograd, Serbia'],
[42.5030333,-89.0309048, '700 College St, Beloit, WI 53511, USA'],
[53.8930389,27.5455567, 'Prospekt Nezavisimosti 4, Minsk, Belarus'],
[31.262218,34.801461, 'שד בן-גוריון 1, באר שבע, Israel'],
[10.6779085,78.74454879999999, 'Palkalaiperur, Tiruchirappalli, Tamil Nadu 620024, India'],
[42.3504997,-71.1053991, 'Boston, MA 02215, USA'],
[35.3050053,-120.6624942, 'San Luis Obispo, CA 93407, USA'],
[34.1821786,-117.3235324, '5500 University Pkwy, San Bernardino, CA 92407, USA'],
[40.7315104,-111.8551883, '1840 S 1300 E, Salt Lake City, UT 84105, USA'],
[40.8075355,-73.9625727, '116th St & Broadway, New York, NY 10027, USA'],
[52.074461,-0.629289, 'College Road, Cranfield MK43 0AL, United Kingdom'],
[50.1030364,14.3912841, 'Zikova 1903/4, 166 36 Praha 6, Czechia'],
[43.7044406,-72.2886935, 'Hanover, NH 03755, USA'],
[37.3195396,-122.0450548, '21250 Stevens Creek Blvd, Cupertino, CA 95014, USA'],
[51.3767813,7.4955588, 'Universitätsstraße 11, 58097 Hagen, Germany'],
[48.4331922,35.0427966, 'Haharina Ave, 72, Dnipropetrovsk, Dnipropetrovsk Oblast, Ukraine, 49000'],
[38.4306911,27.1369201, 'Kültür Mahallesi, Cumhuriyet Blv No:144, 35220 Konak/İzmir, Turkey'],
[39.9566127,-75.18994409999999, '3141 Chestnut St, Philadelphia, PA 19104, USA'],
[30.2849185,-97.7340567, 'Austin, TX 78712, USA'],
[36.0014258,-78.9382286, 'Durham, NC 27708, USA'],
[45.786447,4.764139000000001, '23 Avenue Guy de Collongue, 69130 Écully, France'],
[48.7085753,2.163919, '3 Rue Joliot Curie, 91190 Gif-sur-Yvette, France'],
[36.1027527,-79.50235669999999, '50 Campus Drive, Elon, NC 27244, USA'],
[55.4884528,8.4470501, 'Erhvervsakademi Sydvest, Spangsbjerg Kirkevej, 6700 Esbjerg, Denmark'],
[-2.1481458,-79.9644885, 'Vía Perimetral 5, Guayaquil, Ecuador'],
[51.2473822,6.7916469, 'Münsterstraße 156, 40476 Düsseldorf, Germany'],
[47.72336,13.0871409, 'Urstein Süd 1, 5412 Puch bei Hallein, Austria'],
[-23.6958579,-46.5464383, 'Av. Pereira Barreto, 400 - Baeta Neves, São Bernardo do Campo - SP, 09634-050, Brazil'],
[45.2461012,19.8516968, 'Trg Dositeja Obradovića 6, Novi Sad 106314, Serbia'],
[40.752182,-73.422446, '2350 Broadhollow Rd, Farmingdale, NY 11735, USA'],
[-19.8690878,-43.9663841, 'Av. Pres. Antônio Carlos, 6627 - Pampulha, Belo Horizonte - MG, 31270-901, Brazil'],
[26.373528,-80.10221779999999, '777 Glades Rd, Boca Raton, FL 33431, USA'],
[42.7793667,-72.0560856, '40 University Dr, Rindge, NH 03461, USA'],
[26.1535593,91.6630314, 'The Registrar, Gauhati University, Gopinath Bordoloi Nagar, Guwahati, Assam 781014, India'],
[38.8315541,-77.3120885, '4400 University Dr, Fairfax, VA 22030, USA'],
[38.8977953,-77.0129087, '600 New Jersey Ave NW, Washington, DC 20001, USA'],
[33.753068,-84.38528190000001, 'Atlanta, GA 30302, USA'],
[42.9097484,-85.7630885, 'Grandville, MI, USA'],
[50.8748769,4.7077753, 'Andreas Vesaliusstraat 13, 3000 Leuven, Belgium'],
[21.0056183,105.8433475, '1 Đại Cồ Việt, Bách Khoa, Hai Bà Trưng, Hà Nội, Vietnam'],
[31.7945578,35.2414009, 'Jerusalem'],
[17.445388,78.3482302, 'Gachibowli, Hyderabad, Telangana 500032, India'],
[26.5123388,80.2329, 'Kalyanpur, Kanpur, Uttar Pradesh 208016, India'],
[59.3954769,24.6643815, 'Raja 4, 12616 Tallinn, Estonia'],
[39.16609,-86.5265478, '107 S Indiana Ave, Bloomington, IN 47405, USA'],
[45.4376934,12.3223365, 'S. Croce, 191, 30135 Venezia VE, Italy'],
[41.8348731,-87.6270059, '10 W 35th St, Chicago, IL 60616, USA'],
[40.5122833,-88.9946702, '100 N University St, Normal, IL 61761, USA'],
[41.8348731,-87.6270059, '10 W 35th St, Chicago, IL 60616, USA'],
[22.3149274,87.31053109999999, 'Kharagpur, West Bengal 721302, India'],
[23.8143819,86.44120219999999, 'Police Line, Sardar Patel Nagar, Hirapur, Dhanbad, Jharkhand 826004, India'],
[39.16609,-86.5265478, '107 S Indiana Ave, Bloomington, IN 47405, USA'],
[39.16609,-86.5265478, '107 S Indiana Ave, Bloomington, IN 47405, USA'],
[45.4946761,-73.5622961, '1100 Rue Notre-Dame Ouest, Montréal, QC H3C 1K3, Canada'],
[37.3686167,-121.9695133, '2400 Walsh Ave, Santa Clara, CA 95051, USA'],
[18.487876,-69.96229199999999, 'Av. de Los Próceres 49, Santo Domingo 10602, Dominican Republic'],
[17.445388,78.3482302, 'Gachibowli, Hyderabad, Telangana 500032, India'],
[52.2766124,104.2777287, 'Ulitsa Karla Marksa, 1, Irkutsk, Irkutskaya oblast, Russia, 664003'],
[22.4998759,88.3714991, '188, Raja S.C. Mallick Rd, Kolkata, West Bengal 700032, India'],
[17.494568,78.39205559999999, 'Kukatpally, Hyderabad, Telangana 500085, India'],
[28.540214,77.1661949, 'New Mehrauli Road, Munirka, New Delhi, Delhi 110067, India'],
[32.4950392,35.9912257, 'Ar Ramtha, Irbid, Jordan'],
[39.1974437,-96.5847249, 'Manhattan, KS 66506, USA'],
[2.7350439,101.7010435, 'Kuala Lumpur Intl Airport (KUL), 64000 Sepang, Selangor, Malaysia'],
[42.290035,-85.598145, '1200 Academy St, Kalamazoo, MI 49006, USA'],
[54.898991,23.912825, 'K. Donelaičio g. 73, Kaunas 44249, Lithuania'],
[54.898991,23.912825, 'K. Donelaičio g. 73, Kaunas 44249, Lithuania'],
[55.790447,49.1214349, 'Kremlyovskaya St, 18, Kazan, Respublika Tatarstan, Russia, 420008'],
[41.1490629,-81.34146489999999, '800 E Summit St, Kent, OH 44240, USA'],
[50.004537,36.228139, 'Svobody Square, 4, Kharkiv, Kharkiv Oblast, Ukraine, 61000'],
[13.6518454,100.4950102, '126 Pracha Uthit Rd, Khwaeng Bang Mot, Khet Thung Khru, Krung Thep Maha Nakhon 10140, Thailand'],
[53.270796,69.369861, '53°1614.9"N 69°2211.5"E, Kazakhstan'],
[50.4488824,30.4572542, 'просп. Перемоги, 37, Kyiv, Ukraine, 03056'],
[50.4488824,30.4572542, 'просп. Перемоги, 37, Kyiv, Ukraine, 03056'],
[50.4420868,30.5104023, 'Volodymyrska St, 60, Kyiv, Ukraine, 01033'],
[46.4667708,-80.9742332, '935 Ramsey Lake Rd, Sudbury, ON P3E 2C6, Canada'],
[10.4729537,-66.8931631, 'Avenida Francisco Lazo Martí, Caracas 1040, Distrito Capital, Venezuela'],
[51.7537146,19.4517176, 'Stefana Żeromskiego 116, 90-924 Łódź, Poland'],
[49.8406108,24.0225099, 'Universytetska St, 1, Lviv, Lviv Oblast, Ukraine, 79000'],
[42.701848,-84.4821719, '220 Trowbridge Rd, East Lansing, MI 48824, USA'],
[13.0660293,80.28317190000001, 'Navalar Nagar, Chepauk, Triplicane, Chennai, Tamil Nadu 600005, India'],
[53.42182949999999,58.98138409999999, 'Prospekt Lenina, 38, Magnitogorsk, Chelyabinskaya oblast, Russia, 455000'],
[34.304073,48.8452846, 'Hamadan Province, Malayer, University Blvd, Iran'],
[39.4145456,-81.4491067, '215 5th St, Marietta, OH 45750, USA'],
[24.4335115,54.6176592, 'Masdar City,Khalifa City A,Opp - Airport Road Home WTC AUH - Abu Dhabi - United Arab Emirates'],
[44.8195126,20.459315, 'Studentski trg 16, Beograd 105104, Serbia'],
[42.701848,-84.4821719, '220 Trowbridge Rd, East Lansing, MI 48824, USA'],
[39.8956446,32.7778538, 'Üniversiteler Mh., Eskişehir Yolu No:1, 06800 Çankaya/Ankara, Turkey'],
[37.953451,-91.7755727, '1201 N State St, Rolla, MO 65409, USA'],
[-37.9105238,145.1362182, 'Scenic Blvd, Clayton VIC 3800, Australia'],
[-37.9105238,145.1362182, 'Scenic Blvd, Clayton VIC 3800, Australia'],
[-38.311211,146.429409, 'Northways Rd, Churchill VIC 3842, Australia'],
[25.6515649,-100.28954, 'Av. Eugenio Garza Sada 2501 Sur, Tecnológico, 64849 Monterrey, N.L., Mexico'],
[55.649567,37.6638742, 'Kashira Highway, 31, Moskva, Russia, 115409'],
[55.930467,37.515921, 'Institutskiy Pereulok, 9, Dolgoprudny, Moskovskaya oblast, Russia, 141701'],
[55.70393490000001,37.5286696, 'Ulitsa Leninskiye Gory, 1, Moskva, Russia, 119991'],
[22.2534697,84.9011321, 'Sector - 2, Rourkela, Odisha 769008, India'],
[40.72951339999999,-73.9964609, 'New York, NY 10003, USA'],
[21.1468555,79.050062, 'Amravati Road, Ram Nagar, Nagpur, Maharashtra 440033, India'],
[1.3483099,103.6831347, '50 Nanyang Ave, Singapore 639798'],
[31.3961507,75.5353566, 'N.I.T. Post Office, G T Road, Jalandhar, Punjab 144011, India'],
[25.0173405,121.5397518, 'No. 1, Section 4, Roosevelt Rd, Da’an District, Taipei City, Taiwan 10617'],
[-12.024022,-77.0481441, 'Av. Túpac Amaru s/n, Rimac, Lima 25, Perú, Av. Tupac Amaru 210, Rímac Lima 25, Peru'],
[41.77575969999999,-88.14332, '30 N Brainard St, Naperville, IL 60540, USA'],
[42.3398067,-71.0891717, '360 Huntington Ave, Boston, MA 02115, USA'],
[42.0564594,-87.67526699999999, '633 Clark St, Evanston, IL 60208, USA'],
[55.1372019,36.6064735, 'Студенческий городок, 1, Obninsk, Kaluzhskaya oblast, Russia, 249034'],
[36.8856104,-76.3067777, '5115 Hampton Blvd, Norfolk, VA 23529, USA'],
[42.2586823,-121.7836222, '3201 Campus Dr, Klamath Falls, OR 97601, USA'],
[19.4436005,-70.6843785, 'Autopista Duarte Km 1 1/2, Santiago De Los Caballeros 51000, Dominican Republic'],
[35.8012314,51.5028533, 'Tehran Province, Tehran, اتوبان ارتش کوی نفت, Nakhl St, Iran'],
[40.7982133,-77.8599084, 'Old Main, State College, PA 16801, USA'],
[45.4781071,9.2272764, 'Piazza Leonardo da Vinci, 32, 20133 Milano MI, Italy'],
[44.4386064,26.0494925, 'Splaiul Independenței 313, București 060042, Romania'],
[45.7537285,21.2251368, 'Piața Victoriei 2, Timișoara 300006, Romania'],
[12.0219328,79.85748319999999, 'Kalapet, Puducherry, 605014, India'],
[-33.4411279,-70.6407933, 'Av Libertador Bernardo OHiggins 340, Santiago, Región Metropolitana, Chile'],
[45.511833,-122.6842319, '1825 SW Broadway, Portland, OR 97201, USA'],
[39.7738832,-86.1763393, '420 University Blvd, Indianapolis, IN 46202, USA'],
[12.9237077,77.4986878, 'Mysuru Road, R. V. Vidyanikethan Post, Bengaluru, Karnataka 560059, India'],
[42.730172,-73.67880300000002, '110 8th St, Troy, NY 12180, USA'],
[41.0815079,-74.1746234, '505 Ramapo Valley Rd, Mahwah, NJ 07430, USA'],
[43.0861017,-77.6705143, '1 Lomb Memorial Dr, Rochester, NY 14623, USA']
];