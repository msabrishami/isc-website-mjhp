
# html header, including title, tab navigation
# Arguments: title, title
html_head = '''
<!DOCTYPE html>
<html lang="en">
    
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />

    <title>{}</title>

    <!-- Favicons -->
    <!-- <link href="assets/img/favicon.png" rel="icon" />
    <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon" /> -->
    
    <!--  scripts -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
    <script src="//code.iconify.design/1/1.0.6/iconify.min.js"></script>
    
    <!--  CSS Files -->
    <link
      href="assets/libraries/bootstrap/css/bootstrap.min.css"
      rel="stylesheet"
    />
    
    <!-- Main CSS File -->
    <link href="assets/css/style.css" rel="stylesheet" />
</head>




<body>
    
    
<!-- ======= Header ======= -->
<!-- Header is here -->
<!-- ======= End Header ======= -->


<main id="main">
    

    <!-- ======= Title ======= -->
    <div class="container">
        <div class="main-title mb-2">
            <a class="back-to-IP" href="https://www.iranianstudentsca.org/information-portal"><i class="iconify" data-icon="mdi-chevron-left"></i>
                back
                <span class="d-none d-lg-inline-block">&nbsp;to information portal</span>
            </a>
            <h1>{}</h1>
            <a class="logo" href="https://www.iranianstudentsca.org/">
                <img src="https://images.squarespace-cdn.com/content/v1/6174deaec8e33e3a7fc7bf7b/58ce6a7a-2109-40ca-91a0-6e060c4e2fd3/Icon.png?format=1500w" alt="" />
            </a>
        </div>
    </div>
    <!-- ======= End Title ====== -->


    '''

html_tab_nav_head = '''
    <!-- ======= Tabs Navigation ======= -->
    <div class="tab-navigation">
        <div class="container">
            <ul class="nav nav-pills" id="pills-tab" role="tablist">
    '''

# Creating the tab
# Arguments: h2-tag, h2-tag, h2-tag, h2-name
html_tab_nav = '''
                
                <!-- Instance for a tab in tab navigator -->
                <li class="nav-item" role="presentation">
                    <button
                        class="nav-link {}"
                        id="pills-{}-tab"
                        data-bs-toggle="pill"
                        data-bs-target="#pills-{}"
                        type="button"
                        role="tab"
                        aria-controls="pills-{}"
                        aria-selected="true">
                        {}
                    </button>
                </li>
                '''

html_tab_nav_tail = '''
            </ul>
        </div>
    </div>
    <!-- ====== End Tabs Navigation ====== -->

    '''

html_tab_content_head = '''
    <div class="container">
        <div class="tab-content" id="pills-tabContent">
        '''

   
# HTML for creating h1 
# show active / None, h1-id, h1-id, h1-name
# show active
html_tab_content = '''
            <!-- ==== Starting a new tab (H1) ==== -->
            <!-- Connecting Tab's show on/off to Tab Navigator -->
            <div class="tab-pane fade {}"
                id="pills-{}"
                role="tabpanel"
                aria-labelledby="pills-{}-tab"
                tabindex="0">
                
                <!-- == H1.title, outline of H2s ==== -->
                <section>
                    
                    <!-- ==== Tab title ==== -->
                    <div class="tab-title">
                        <h2>{}</h2>
                    </div>

                    <!-- ==== Tab Outline (list of H2s) ==== -->
                    <div class="tab-outlines">
'''


top_html = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />

    <title>{}</title>

    <!-- Favicons -->
    <!-- <link href="assets/img/favicon.png" rel="icon" />
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon" /> -->

    <!--  scripts -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
    <script src="//code.iconify.design/1/1.0.6/iconify.min.js"></script>

    <!--  CSS Files -->
    <link
      href="assets/libraries/bootstrap/css/bootstrap.min.css"
      rel="stylesheet"
    />

    <!-- Main CSS File -->
    <link href="assets/css/style.css" rel="stylesheet" />

    <!-- =======================================================
  ======================================================== -->
  </head>

  <body>
    <!-- ======= Header ======= -->

    <!-- End Header -->

    <main id="main">
      <!-- ======= Title ======= -->
      <div class="container">
        <div class="main-title mb-2">
          <a class="back-to-IP" href="https://www.iranianstudentsca.org/information-portal">
            <i class="iconify" data-icon="mdi-chevron-left"></i>
            back
            <span class="d-none d-lg-inline-block">&nbsp;to information portal</span>
          </a>
          <h1>{}</h1>
          <a class="logo" href="https://www.iranianstudentsca.org/">
            <img src="https://images.squarespace-cdn.com/content/v1/6174deaec8e33e3a7fc7bf7b/58ce6a7a-2109-40ca-91a0-6e060c4e2fd3/Icon.png?format=1500w" alt="" />
          </a>
        </div>
      </div>

      <!-- End Title -->

      <!-- ======= Tabs Navigation ======= -->
      <div class="tab-navigation">
        <div class="container">
          <ul class="nav nav-pills" id="pills-tab" role="tablist">
            <li class="nav-item" role="presentation">
              <button
                class="nav-link active"
                id="pills-bank-tab"
                data-bs-toggle="pill"
                data-bs-target="#pills-bank"
                type="button"
                role="tab"
                aria-controls="pills-bank"
                aria-selected="true"
              >
                bank account
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button
                class="nav-link"
                id="pills-score-tab"
                data-bs-toggle="pill"
                data-bs-target="#pills-score"
                type="button"
                role="tab"
                aria-controls="pills-score"
                aria-selected="false"
              >
                credit score
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button
                class="nav-link"
                id="pills-card-tab"
                data-bs-toggle="pill"
                data-bs-target="#pills-card"
                type="button"
                role="tab"
                aria-controls="pills-card"
                aria-selected="false"
              >
                credit cards
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button
                class="nav-link"
                id="pills-tax-tab"
                data-bs-toggle="pill"
                data-bs-target="#pills-tax"
                type="button"
                role="tab"
                aria-controls="pills-tax"
                aria-selected="false"
              >
                tax
              </button>
            </li>
          </ul>
        </div>
      </div>
      <!-- End Tabs Navigation -->
      '''



tab_html = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />

    <title>{}</title>

    <!-- Favicons -->
    <!-- <link href="assets/img/favicon.png" rel="icon" />
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon" /> -->

    <!--  scripts -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
    <script src="//code.iconify.design/1/1.0.6/iconify.min.js"></script>

    <!--  CSS Files -->
    <link
      href="assets/libraries/bootstrap/css/bootstrap.min.css"
      rel="stylesheet"
    />

    <!-- Main CSS File -->
    <link href="assets/css/style.css" rel="stylesheet" />

    <!-- =======================================================
  ======================================================== -->
  </head>

  <body>
    <!-- ======= Header ======= -->

    <!-- End Header -->

    <main id="main">
      <!-- ======= Title ======= -->
      <div class="container">
        <div class="main-title mb-2">
          <a class="back-to-IP" href="https://www.iranianstudentsca.org/information-portal">
            <i class="iconify" data-icon="mdi-chevron-left"></i>
            back
            <span class="d-none d-lg-inline-block">&nbsp;to information portal</span>
          </a>
          <h1>{}</h1>
          <a class="logo" href="https://www.iranianstudentsca.org/">
            <img src="https://images.squarespace-cdn.com/content/v1/6174deaec8e33e3a7fc7bf7b/58ce6a7a-2109-40ca-91a0-6e060c4e2fd3/Icon.png?format=1500w" alt="" />
          </a>
        </div>
      </div>

      <!-- End Title -->

      <!-- ======= Tabs Navigation ======= -->
      <div class="tab-navigation">
        <div class="container">
          <ul class="nav nav-pills" id="pills-tab" role="tablist">
            <li class="nav-item" role="presentation">
              <button
                class="nav-link active"
                id="pills-bank-tab"
                data-bs-toggle="pill"
                data-bs-target="#pills-bank"
                type="button"
                role="tab"
                aria-controls="pills-bank"
                aria-selected="true"
              >
                bank account
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button
                class="nav-link"
                id="pills-score-tab"
                data-bs-toggle="pill"
                data-bs-target="#pills-score"
                type="button"
                role="tab"
                aria-controls="pills-score"
                aria-selected="false"
              >
                credit score
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button
                class="nav-link"
                id="pills-card-tab"
                data-bs-toggle="pill"
                data-bs-target="#pills-card"
                type="button"
                role="tab"
                aria-controls="pills-card"
                aria-selected="false"
              >
                credit cards
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button
                class="nav-link"
                id="pills-tax-tab"
                data-bs-toggle="pill"
                data-bs-target="#pills-tax"
                type="button"
                role="tab"
                aria-controls="pills-tax"
                aria-selected="false"
              >
                tax
              </button>
            </li>
          </ul>
        </div>
      </div>
      <!-- End Tabs Navigation -->
      '''

html_footer ='''

<!-- ======= Footer ======= -->
<footer>
    <div class="container">
        <div class="row">
            <div class="col-lg-6 col-md-5 d-flex align-items-center">
                <div>
                    <p class="h6 mb-3 mx-auto mb-md-2">Iranian Students of California</p>
                    <p class="sponsor small fw-light">
                    Information Portal is sponsored by
                    <a class="d-block d-md-inline" 
                        href="https://parsequalitycenter.org/" 
                        target="_blank">Pars Equality Center
                    </a>
                    </p>
                </div>
            </div>
            <div class="col-lg-6 col-md-7">
                <div class="social-media-links">
                    <a href="https://www.instagram.com/iranian.students.ca/" target="_blank"> <i class="iconify" data-icon="mdi-instagram"></i> </a>
                    <a href="https://www.linkedin.com/company/iranian-students-of-california/" target="_blank"> <i class="iconify" data-icon="mdi-linkedin"></i> </a>
                    <a href="https://www.facebook.com/Iranian.Students.CA/" target="_blank"> <i class="iconify" data-icon="mdi-facebook"></i> </a>
                    <a href="https://twitter.com/IranStudentsCA" target="_blank"> <i class="iconify" data-icon="mdi-twitter"></i> </a>
                    <a href="https://www.youtube.com/channel/UCP48hfBfB9mC63UI35rE6mw" target="_blank"> <i class="iconify" data-icon="mdi-youtube"></i> </a>
                </div>
            </div>
        </div>
    </div>
</footer>
<!-- End Footer -->

'''

tail_text = '''
</main>
<!-- End #main -->
''' + html_footer + '''

<!-- JS Files -->
<script src="assets/libraries/bootstrap/js/bootstrap.bundle.min.js"></script>

<!-- Main JS File -->
<script src="assets/js/main.js"></script>

</body>
</html>
'''

