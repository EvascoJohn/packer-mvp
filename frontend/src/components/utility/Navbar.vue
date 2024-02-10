<template>
    <div class="w-screen h-[40px] bg-blue-400 flex items-center justify-between p-5 text-sm">
        <div class="flex items-center gap-5">
            <div class="flex flex-col-2 items-center"> <!-- Added flex-col class -->
                <span class="material-icons md-18">
                    home
                </span>
                Home
            </div>
            <div>
                <span>Contact Us</span>
            </div>
            <div>
                <span>About</span>
            </div>
        </div>
        <div class="flex gap-5">
            <div class="bg-blue-500 rounded p-1 text-white">
                <div v-if="true">
                    <span>Login</span>
                </div>
                <div v-else>
                    <span>Logged</span>
                </div>
            </div>
            <div class="bg-blue-500 rounded p-1 text-white">
                <span>Register</span>
            </div>
        </div>
    </div>
</template>

<style>
/* Rules for sizing the icon. */
.material-icons.md-18 { font-size: 18px; }
.material-icons.md-24 { font-size: 24px; }
.material-icons.md-36 { font-size: 36px; }
.material-icons.md-48 { font-size: 48px; }

/* Rules for using icons as black on a light background. */
.material-icons.md-dark { color: rgba(0, 0, 0, 0.54); }
.material-icons.md-dark.md-inactive { color: rgba(0, 0, 0, 0.26); }

/* Rules for using icons as white on a dark background. */
.material-icons.md-light { color: rgba(255, 255, 255, 1); }
.material-icons.md-light.md-inactive { color: rgba(255, 255, 255, 0.3); }
</style>