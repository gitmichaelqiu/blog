---
comments: true
---

# Browser

Browser is the gate to the internet. It is one of the a few apps that always run in your computer. I have used many browseres, and I want to share my own experiences.

## Microsoft Edge

Edge is a highly optimized one. It has good memory management, low battery consumption, web rendering performances. It is also packed with tons of novel features that makes it doesn't feel like a product of Microsoft.

If you live in Mainland China, it's unique advantage to Chrome is that all synchronizations can be done normally (doesn't like Chrome where it depends on Google services).

Edge has been my default browser for a long while. It just works. It satisfies all of your basic needs.

## Arc & Dia

But it is not until Arc went viral in 2023 that I see a truly revolutionary redesign over the web browsing experiences: peek, spaces, nestable folders, little Arc. The built-in AI webpage summarization feature immediately reduces your time spending on information extraction.

But its story ended after they announced Dia browser, that the team behind it, the New York Browser Company, would no longer pack new features into it. Dia was merely a concept, and not even built on Arc. It was basically plain Chromium plus some novel AI features, but the raw browsing experiences that Arc has revolutionized were completely dumped by the team. Dia, to be honest, is not a product in my eyes. In most of the time, you are not that dependent on AI. Mostly you are asking AI to summarize websites and ask webpage relevant questions. This can be done by browser extension and third party apps, not a sufficient reason to let you root in Dia.

AI products have been hyped since 2023. NYBC chose to chase this trend, but from scratch. Though they are still putting Arc features to Dia, the experience is unmatched and the AI feature has broken the balance between human and machine browsing: Dia is bloated by AI features.

## Zen

After NYBC ditches Arc, a firefox-based open-sourced alternative Zen appeared. At first sight, it implements many of the features of Arc: glance, spaces, nestable folders, essential tabs... But it is not packed with hyped AI features. As its slogan says, it gives you a cool browsing experience.

Zen was my main browser for half a year. It gave me what Arc had, with more customizations. Every hotkey can be customized, all theme elements can be modified through Zen mods and Sine mods.

I even opened pull requests to suggest fixes to the browser on GitHub. I truly loved the chilled experiences, as I feel more productivity with Zen. With my own app [SpaceSwitcher](https://spaceswitcher.mqiu.dev/), Zen would even automatically switch spaces depending on active macOS virtual space. With the folders, I nearly forgot bookmarks. Folders are far more convenient and portable. For instance, I can clearly organize my tabs during research into different folders. It is not like bookmarks where you need to reopen them. Folders are instantly accessible.

However, all of these do not make Zen perfect: you would observe that I use past tenses when writing the above reviews. Yes, it provides the coolest browsing experiences I have ever seen, but the browser itself is not "cool" enough: it is a resource killer.

If you check Zen's source code, you will find that its UI is implemented using CSS and other frontend technologies. Every time your cursor moves, the browser gives a UI refresh. Basically it is constantly refreshing, and it can be a headache for macOS resource allocator: it constantly occupies a large amount of computing resources, and the allocator is hard to optimize its usage.

Expecially for a student like me, I am sensitive to battery usage. My laptop is running on its battery for most of the times in school. Zen drains my battery quickly. Meanwhile, Zen uses Firefox engine, and Firefox is know to have poor performance on js and websites. Websites are more optimized on Chromium because it is the industrial standard.

Another thing that goes wrong with Firefox is the extension ecosystem. In April 2026, the Shortkeys extension becomes unusable due to its building on Firefox. The development team of Shortkeys has updated their extension and pushed the revision request to the web store maintainer. However, due to the infamous efficiency of Mozilla organization, the update is not approved for at least a month, not until when I am writing this article. I rely on this extension to quickly close designated tabs and do other actions, and it being unusable completely disrupts my workflows.

Mozilla was praised for their focus on user privacy. But they recently forced to integrate AI models into Firefox. These local models are barely usable: they are small, and the usage case is niche. It is awkward because Firefox does not give it enough native supports, almost like an extension. In 2026, Mozilla still has not added native Progress Web App support to Firefox. In many cases I prefer a standalone application rather than filling my browsers with tabs. PWA is an important part of my workflow: both Safari and Chromium browser have the support, and it is extremely disappointing that Firefox fails to deliver it.

My patience over Mozilla has been completely crushed: they are just so inefficient and incapable, wasting the supportive finance from Google. Years ago, Firefox was known for having less RAM usage, but such gap now is closed by Chromium team's efforts on optimization, while Firefox is merely experimenting on some UI refreshes with no significant improvements.

Of cource, it is not Zen's fault. Matter of fact, Zen does have its own reason for choosing Firefox: privacy conservation and highly customizable. But these two do not outweigh the disadvantages in battery consumption and RAM usage: I would rather to have a longer access to the browser than having a good time.

After Chrome offcially introduced native vertical tabs, I entered a time when I constantly switching between Zen, Chrome, and Arc. Chrome is poorly customizable, and that I have to click to expand/collapse vertical tab bar can be inefficient for me.

## Helium

But in early 2026, a new open-sourced competitor emerged: Helium browser. It is a simple product: it uses ungoogled Chromium so bloated Google services are removed. It natively supports Cmd+S to toggle vertical bar, Cmd+Shift+C to copy the website link... and most importantly, it removes every possible pixels of UI so it shows more on webpages. The focus on the web itself is so clear. Meanwhile, it is one of the mostly optimized browser yet. Ungooled Chromium kernel means it uses even less resources than Chrome and Edge.

Unlike Zen, which uses CSS to render UI, helium uses native C++ patches to modify interfaces - this means the UI is native. Safari is the only possible winner above Helium on battery consumption and RAM usage.

But I have to admit many features expected by me are still missing in Helium: glances and nestable folders. The good news is that it is an open-sourced project, and the support from community developers allows the Imputnet Team behind Helium to build faster - though currently the development pace is slower compared to Zen's progress.

It is interesting that when you check Helium GitHub repostiory's issues page: users have been posting feature requests on Arc/Zen features. It is clear that many users are migrated from Zen - just like me - and we want a browser highly optimized with cool features. Helium is promising on this, because the team's philosophy is C++ patches. But it also means it is harder to develop compared to CSS used by Zen.

Helium has the potential, and it has become my main browser. The only thing I wish is that Helium comes with more customizations on hotkeys and more Zen features. And I do admit that: I am merely looking for an optimized Chromium Zen. I want a chilling browser experiences, but not at cost of the basic performances.

Let's see what Imputnet can do.
