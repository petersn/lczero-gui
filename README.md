## lczero-gui

Simple program to watch self-play games generate.

![lczero-gui demo](/docs/demo1.gif?raw=true "lczero-gui demo")

## To use

### Step 1:

First you must apply a patch to `leela-chess` to make it output the moves it actually picks while generating training games.
(The default principal variation printing isn't good enough, because noise makes it deviate from the printed PV moves.)

The following patch suffices:

```diff
diff --git a/src/UCI.cpp b/src/UCI.cpp
index e55ab00..a3a5390 100644
--- a/src/UCI.cpp
+++ b/src/UCI.cpp
@@ -148,6 +148,9 @@ int play_one_game(BoardHistory& bh) {
     Move move = search->think(bh.shallow_clone());
 
     bh.do_move(move);
+
+    string move_string{UCI::move(move)};
+    myprintf_so("info string picked %s\n", move_string.c_str());
   }
 
   // Game termination as draw
```

You can also find this patched version in [my fork](https://github.com/petersn/leela-chess) of `leela-chess`.

Once you have compiled the `lczero` binary, copy both it and the `client` binary into this directory.

### Step 2:

Simply install all the dependencies, and launch the application:

```
    $ npm install
    $ npm start
```

My GUI currently doesn't show good diagnostics for when it's downloading new networks, so it might take a minute or two for the pieces to start moving while it's downloading.
(TODO: Patch the client to print progress info, so my GUI can show a download bar.)

### Documentation

This code is currently horrifically undocumented.
I literally wrote it in a morning, and it requires a two-line patch to `lczero` to get it to output the moves it's selecting.
TODO: Add everything else.

