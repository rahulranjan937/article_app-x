from hashlib import sha256
import mysql.connector
from config import dbHost, dbuser, dbpasswd, dbport, db

mydb = mysql.connector.connect(host=dbHost, user=dbuser, password=dbpasswd, port=dbport, database=db)

mycursor = mydb.cursor()

# Insert Article into DB

sql = "INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)"

val = [
    (
        "lorem ipsum",
        "lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet.",
        "John Doe",
    ),
    (
        "Learn Python",
        "Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.",
        "Jane Doe",
    ),
    (
        "Learn JavaScript",
        "JavaScript is a lightweight, interpreted programming language. It is designed for creating network-centric applications. It is complimentary to and integrated with Java. JavaScript is very easy to implement because it is integrated with HTML. It is open and cross-platform.",
        "John Doe",
    ),
    (
        "Learn Java",
        "Java is a high-level programming language developed by Sun Microsystems. It was originally designed for developing programs for set-top boxes and handheld devices, but later became a popular choice for creating web applications.",
        "Jane Doe",
    ),
    (
        "Learn C++",
        "C++ is a middle-level programming language developed by Bjarne Stroustrup starting in 1979 at Bell Labs. C++ runs on a variety of platforms, such as Windows, Mac OS, and the various versions of UNIX.",
        "John Doe",
    ),
    (
        "Learn C#",
        "C# is a modern, object-oriented programming language developed by Microsoft. C# (pronounced C-sharp) is a general-purpose, multi-paradigm programming language that encompasses strong typing, imperative, declarative, functional, generic, object-oriented (class-based), and component-oriented programming disciplines.",
        "Jane Doe",
    ),
    (
        "Learn Ruby",
        "Ruby is a dynamic, reflective, object-oriented, general-purpose programming language. It was designed and developed in the mid-1990s by Yukihiro Matsumoto in Japan.",
        "John Doe",
    ),
    (
        "Learn PHP",
        "PHP is a server scripting language, and a powerful tool for making dynamic and interactive Web pages. PHP is a widely-used, free, and efficient alternative to competitors such as Microsoft's ASP.",
        "Jane Doe",
    ),
    (
        "Learn Perl",
        'Perl is a family of two high-level, general-purpose, interpreted, dynamic programming languages. "Perl" refers to Perl 5, but from 2000 to 2019 it also referred to its redesigned "sister language", Perl 6, before the latter\'s name was officially changed to Raku in October 2019.',
        "John Doe",
    ),
    (
        "Learn Swift",
        "Swift is a powerful and intuitive programming language for iOS, macOS, tvOS, and watchOS. Writing Swift code is interactive and fun, the syntax is concise yet expressive, and Swift includes modern features developers love.",
        "Jane Doe",
    ),
    (
        "Learn Kotlin",
        "Kotlin is a cross-platform, statically typed, general-purpose programming language with type inference. Kotlin is designed to interoperate fully with Java, and the JVM version of its standard library depends on the Java Class Library, but type inference allows its syntax to be more concise.",
        "John Doe",
    ),
    (
        "Learn Go",
        "Go is an open source programming language that makes it easy to build simple, reliable, and efficient software. Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction.",
        "Jane Doe",
    ),
    (
        "Learn Rust",
        "Rust is a systems programming language that runs blazingly fast, prevents segfaults, and guarantees thread safety. Rust is a multi-paradigm programming language focused on performance and safety, especially safe concurrency.",
        "John Doe",
    ),
    (
        "Learn Scala",
        "Scala combines object-oriented and functional programming in one concise, high-level language. Scala's static types help avoid bugs in complex applications, and its JVM and JavaScript runtimes let you build high-performance systems with easy access to huge ecosystems of libraries.",
        "Jane Doe",
    ),
    (
        "Learn TypeScript",
        "TypeScript is a typed superset of JavaScript that compiles to plain JavaScript. TypeScript is designed for the development of large applications and transcompiles to JavaScript. As TypeScript is a superset of JavaScript, existing JavaScript programs are also valid TypeScript programs.",
        "John Doe",
    ),
    (
        "Learn Dart",
        "Dart is a client-optimized programming language for fast apps on any platform. Dart is an open-source, scalable programming language, with robust libraries and runtimes, for building web, server, and mobile apps.",
        "Jane Doe",
    ),
    (
        "Learn R",
        "R is a programming language and free software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing. The R language is widely used among statisticians and data miners for developing statistical software and data analysis.",
        "John Doe",
    ),
    (
        "Learn MATLAB",
        "MATLAB is a high-performance language for technical computing. It integrates computation, visualization, and programming in an easy-to-use environment where problems and solutions are expressed in familiar mathematical notation.",
        "Jane Doe",
    ),
    (
        "Learn Ruby on Rails",
        "Ruby on Rails, or Rails, is a server-side web application framework written in Ruby under the MIT License. Rails is a model–view–controller framework, providing default structures for a database, a web service, and web pages.",
        "John Doe",
    ),
    (
        "Learn Django",
        "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.",
        "Jane Doe",
    ),
    (
        "Learn Flask",
        "Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.",
        "John Doe",
    ),
    (
        "Learn Spring",
        "The Spring Framework is an application framework and inversion of control container for the Java platform. The framework's core features can be used by any Java application, but there are extensions for building web applications on top of the Java EE platform.",
        "Jane Doe",
    ),
    (
        "Learn Angular",
        "Angular is a platform and framework for building single-page client applications using HTML and TypeScript. Angular is written in TypeScript. It implements core and optional functionality as a set of TypeScript libraries that you import into your apps.",
        "John Doe",
    ),
    (
        "Learn React",
        "React is a JavaScript library for building user interfaces. It is maintained by Facebook and a community of individual developers and companies. React can be used as a base in the development of single-page or mobile applications.",
        "Jane Doe",
    ),
    (
        "Learn Vue",
        "Vue.js is an open-source model–view–viewmodel JavaScript framework for building user interfaces and single-page applications. It was created by Evan You, and is maintained by him and the rest of the active core team members coming from various companies such as Netlify and Netguru.",
        "John Doe",
    ),
    (
        "Learn Ember",
        "Ember.js is an open-source JavaScript web framework, based on the Model–view–viewmodel pattern. It allows developers to create scalable single-page web applications by incorporating common idioms and best practices into the framework.",
        "Jane Doe",
    ),
    (
        "Learn Backbone",
        "Backbone.js is a JavaScript library with a RESTful JSON interface and is based on the model–view–presenter application design paradigm. Backbone is known for being lightweight, as its only hard dependency is on one JavaScript library, Underscore.js.",
        "John Doe",
    ),
    (
        "Learn Knockout",
        "Knockout is a standalone JavaScript implementation of the Model-View-ViewModel pattern with templates. The underlying principles are therefore: a clear separation between domain data, view components, and data to be displayed.",
        "Jane Doe",
    ),
    (
        "Learn Meteor",
        "Meteor, or MeteorJS, is a free and open-source isomorphic JavaScript web framework written using Node.js. Meteor allows for rapid prototyping and produces cross-platform code. It integrates with MongoDB and uses the Distributed Data Protocol and a publish–subscribe pattern to automatically propagate data changes to clients without requiring the developer to write any synchronization code.",
        "John Doe",
    ),
    (
        "Learn Svelte",
        "Svelte is a free and open-source front end JavaScript framework that is written in TypeScript. It is used to build web applications and is based on component composition. Svelte is a compiler that generates highly efficient vanilla JavaScript code.",
        "Jane Doe",
    ),
    (
        "Learn Express",
        "Express.js, or simply Express, is a back end web application framework for Node.js, released as free and open-source software under the MIT License. It is designed for building web applications and APIs.",
        "John Doe",
    ),
    (
        "Learn Koa",
        "Koa is a web framework for Node.js, created by the team behind Express, which aims to be a smaller, more expressive, and more robust foundation for web applications and APIs. By using async functions, Koa allows you to ditch callbacks and greatly increase error-handling.",
        "Jane Doe",
    ),
    (
        "Learn Hapi",
        "Hapi.js, or simply Hapi, is a rich framework for building applications and services. It enables developers to focus on writing reusable application logic instead of spending time building infrastructure.",
        "John Doe",
    ),
    (
        "Learn Nest",
        "NestJS is a framework for building efficient, scalable Node.js server-side applications. It uses progressive JavaScript, is built with TypeScript and combines elements of OOP (Object Oriented Programming), FP (Functional Programming), and FRP (Functional Reactive Programming).",
        "Jane Doe",
    ),
    (
        "Learn Fastify",
        "Fastify is a web framework highly focused on providing the best developer experience with the least overhead and a powerful plugin architecture. It is inspired by Hapi and Express and is one of the fastest web frameworks in town.",
        "John Doe",
    ),
    (
        "Learn Adonis",
        "AdonisJs is a Node.js web framework with a breath of fresh air and drizzle of elegant syntax on top of it. It offers a stable ecosystem to write server-side web applications so you can focus on business needs over finalizing which package to choose or not.",
        "Jane Doe",
    ),
    (
        "Learn Loopback",
        "LoopBack is a highly extensible, open-source Node.js framework based on Express that enables you to quickly create dynamic end-to-end REST APIs and connect them to data sources such as databases and SOAP or REST services.",
        "John Doe",
    ),
    (
        "Learn Feathers",
        "Feathers is a web-framework for creating real-time applications and REST APIs using JavaScript or TypeScript with Node.js, React Native and the browser.",
        "Jane Doe",
    ),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mydb.close()

mydb.disconnect()
