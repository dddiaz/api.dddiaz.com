---
title: "Covid-19 Genome Analysis"
date: 2020-04-19T18:21:11-07:00
draft: false

tags: ["Genome", "Bioinformatics", "Python", "Jupyter Notebook"]
summary: "Using Python to Inspect the Covid-19 Genome"

header:
    image: "headers/covid.png"
---
To see the original Jupyter Notebook, check it out on Github [Here.](https://github.com/dddiaz/corona/blob/master/notebook.ipynb)
I have included a version of the notebook below.  

{{< rawhtml >}}
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="About:">About:<a class="anchor-link" href="#About:">&#182;</a></h2><p>I want to play around with coronavirus genome. I found this really cool article
<a href="https://blog.floydhub.com/exploring-dna-with-deep-learning/">here</a> where they talked about one-hot encoding a genome 
and plotting it. I want to see if I could apply that to the corona virus. My results are below.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">Bio</span> <span class="kn">import</span> <span class="n">Entrez</span>
<span class="kn">from</span> <span class="nn">Bio</span> <span class="kn">import</span> <span class="n">SeqIO</span>
<span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">re</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">OneHotEncoder</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">LabelEncoder</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.cm</span> <span class="k">as</span> <span class="nn">cm</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Search-NCBI-Data-Online">Search NCBI Data Online<a class="anchor-link" href="#Search-NCBI-Data-Online">&#182;</a></h2><p>Manually compile a list of genome ids we will use. These genome IDs will be used to download the genebank files from the
NCBI database.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Entrez</span><span class="o">.</span><span class="n">email</span> <span class="o">=</span> <span class="s2">&quot;daniel.delvin.diaz+ncbi@gmail.com&quot;</span>  <span class="c1"># Always tell NCBI who you are</span>
<span class="c1"># List of genomes</span>
<span class="c1"># MN908947 -&gt; Ref Genome</span>
<span class="n">genbank_ids</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;MN908947&#39;</span><span class="p">,</span> <span class="s1">&#39;LC534418.1&#39;</span><span class="p">,</span> <span class="s1">&#39;MN985325.1&#39;</span><span class="p">,</span> <span class="s1">&#39;MN988713.1&#39;</span><span class="p">,</span> <span class="s1">&#39;MT077125.1&#39;</span><span class="p">,</span> <span class="s1">&#39;MT093571.1&#39;</span><span class="p">,</span> <span class="s1">&#39;MT044258.1&#39;</span><span class="p">,</span> <span class="s1">&#39;MT039888.1&#39;</span><span class="p">,</span> <span class="s1">&#39;MT039887.1&#39;</span><span class="p">,</span> <span class="s1">&#39;MT027062.1&#39;</span><span class="p">,</span> <span class="s1">&#39;MT019531.1&#39;</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Print-out-one-of-the-results-so-we-can-inspect-it.">Print out one of the results so we can inspect it.<a class="anchor-link" href="#Print-out-one-of-the-results-so-we-can-inspect-it.">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Ref Genome: NC_045512</span>
<span class="k">for</span> <span class="n">g</span> <span class="ow">in</span> <span class="n">genbank_ids</span><span class="p">:</span>
    <span class="n">handle</span> <span class="o">=</span> <span class="n">Entrez</span><span class="o">.</span><span class="n">efetch</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="s2">&quot;nucleotide&quot;</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">g</span><span class="p">,</span> <span class="n">rettype</span><span class="o">=</span><span class="s2">&quot;gb&quot;</span><span class="p">,</span> <span class="n">retmode</span><span class="o">=</span><span class="s2">&quot;text&quot;</span><span class="p">)</span>
    <span class="n">text</span> <span class="o">=</span> <span class="n">handle</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
    <span class="c1"># print(text)</span>
    <span class="k">assert</span> <span class="n">text</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
    <span class="k">break</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Download-all-the-genomes-from-our-search-and-store-them-as-.gb-files.">Download all the genomes from our search and store them as .gb files.<a class="anchor-link" href="#Download-all-the-genomes-from-our-search-and-store-them-as-.gb-files.">&#182;</a></h2><ul>
<li>store them in the generated/ folder</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">count</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">genome_id</span> <span class="ow">in</span> <span class="n">genbank_ids</span><span class="p">:</span>
    <span class="n">filename</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="s2">&quot;.&quot;</span><span class="p">)</span><span class="si">}</span><span class="s1">/generated/genBankRecord_</span><span class="si">{</span><span class="n">genome_id</span><span class="si">}</span><span class="s1">.gb&#39;</span>
    <span class="c1"># Lets not download the genome if we already have it.</span>
    <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Skipping:</span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">filename</span><span class="p">))</span>
        <span class="k">continue</span>

    <span class="n">record</span> <span class="o">=</span> <span class="n">Entrez</span><span class="o">.</span><span class="n">efetch</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="s2">&quot;nucleotide&quot;</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">genome_id</span><span class="p">,</span> <span class="n">rettype</span><span class="o">=</span><span class="s2">&quot;gb&quot;</span><span class="p">,</span> <span class="n">retmode</span><span class="o">=</span><span class="s2">&quot;text&quot;</span><span class="p">)</span>

    <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Writing:</span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">filename</span><span class="p">))</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s1">&#39;w&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">record</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
    <span class="c1"># Im noticing some really wonky file permissions with jupyter notebook and pycharm</span>
    <span class="c1"># going to force it to be this:</span>
    <span class="c1"># Dont forget this is python3 specific syntax</span>
    <span class="n">os</span><span class="o">.</span><span class="n">chmod</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="mo">0o666</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Skipping:/Users/ddiaz/src/corona/generated/genBankRecord_MN908947.gb
Skipping:/Users/ddiaz/src/corona/generated/genBankRecord_LC534418.1.gb
Skipping:/Users/ddiaz/src/corona/generated/genBankRecord_MN985325.1.gb
Skipping:/Users/ddiaz/src/corona/generated/genBankRecord_MN988713.1.gb
Skipping:/Users/ddiaz/src/corona/generated/genBankRecord_MT077125.1.gb
Skipping:/Users/ddiaz/src/corona/generated/genBankRecord_MT093571.1.gb
Skipping:/Users/ddiaz/src/corona/generated/genBankRecord_MT044258.1.gb
Skipping:/Users/ddiaz/src/corona/generated/genBankRecord_MT039888.1.gb
Skipping:/Users/ddiaz/src/corona/generated/genBankRecord_MT039887.1.gb
Skipping:/Users/ddiaz/src/corona/generated/genBankRecord_MT027062.1.gb
Skipping:/Users/ddiaz/src/corona/generated/genBankRecord_MT019531.1.gb
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Download-ref-genome-for-sars-covid-2">Download ref genome for sars-covid-2<a class="anchor-link" href="#Download-ref-genome-for-sars-covid-2">&#182;</a></h2><h2 id="Which-btw-was-made-with-an-Illumina-Genome-Sequencer!-:)-Nice">Which btw was made with an Illumina Genome Sequencer! :) Nice<a class="anchor-link" href="#Which-btw-was-made-with-an-Illumina-Genome-Sequencer!-:)-Nice">&#182;</a></h2><p>Note: I also source controlled this file, so there is no need to download it.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">download_ref_genome</span><span class="p">():</span>
    <span class="n">Entrez</span><span class="o">.</span><span class="n">email</span> <span class="o">=</span> <span class="s2">&quot;daniel.delvin.diaz+ncbi@gmail.com&quot;</span>  <span class="c1"># Always tell NCBI who you are</span>
    <span class="n">record</span> <span class="o">=</span> <span class="n">Entrez</span><span class="o">.</span><span class="n">efetch</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="s2">&quot;nucleotide&quot;</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="s2">&quot;MN908947&quot;</span><span class="p">,</span> <span class="n">rettype</span><span class="o">=</span><span class="s2">&quot;gb&quot;</span><span class="p">,</span> <span class="n">retmode</span><span class="o">=</span><span class="s2">&quot;text&quot;</span><span class="p">)</span>
    <span class="n">filename</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="s2">&quot;.&quot;</span><span class="p">)</span><span class="si">}</span><span class="s1">/ref_genome/genBankRecord_ref.gb&#39;</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s1">&#39;w&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">content</span> <span class="o">=</span> <span class="n">record</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;File Written:</span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">filename</span><span class="p">))</span>

<span class="c1"># Note I have noticed a weird behavior with pycharm + jupyter notebook where you wont see the</span>
<span class="c1"># file locally unless you click out of pycharm then back in.</span>

<span class="c1"># download_ref_genome()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Load-Genome-Functions">Load Genome Functions<a class="anchor-link" href="#Load-Genome-Functions">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">load_ref_genome</span><span class="p">():</span>
    <span class="n">ref_genome_path</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)</span><span class="si">}</span><span class="s2">/ref_genome/genBankRecord_ref.gb&quot;</span>
    <span class="n">ref_genome_seq</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">for</span> <span class="n">seq_record</span> <span class="ow">in</span> <span class="n">SeqIO</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="s2">&quot;./ref_genome/genBankRecord_ref.gb&quot;</span><span class="p">,</span> <span class="s2">&quot;genbank&quot;</span><span class="p">):</span>
        <span class="n">ref_genome_seq</span> <span class="o">=</span> <span class="n">seq_record</span><span class="o">.</span><span class="n">seq</span>
    <span class="k">return</span> <span class="n">ref_genome_seq</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Generic Load Functions</span>
<span class="k">def</span> <span class="nf">load_genomes</span><span class="p">(</span><span class="n">folder_path</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)</span><span class="o">+</span><span class="s2">&quot;/generated/&quot;</span><span class="p">):</span>
    <span class="n">f</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Using folder </span><span class="si">{</span><span class="n">folder_path</span><span class="si">}</span><span class="s2"> to load genomes&quot;</span><span class="p">)</span>
    <span class="k">for</span> <span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">dirnames</span><span class="p">,</span> <span class="n">filenames</span><span class="p">)</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">walk</span><span class="p">(</span><span class="n">folder_path</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">filenames</span><span class="p">:</span>
            <span class="n">f</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">root</span><span class="p">,</span><span class="n">filename</span><span class="p">))</span>
    <span class="n">genomes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">genome_file</span> <span class="ow">in</span> <span class="n">f</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Getting genome from file </span><span class="si">{</span><span class="n">genome_file</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">seq_record</span> <span class="ow">in</span> <span class="n">SeqIO</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">genome_file</span><span class="p">,</span> <span class="s2">&quot;genbank&quot;</span><span class="p">):</span>
            <span class="n">genome_seq</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">seq_record</span><span class="o">.</span><span class="n">seq</span><span class="p">)</span>
            <span class="c1"># Lets assume theres one genome per file</span>
            <span class="n">genomes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">genome_seq</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">genomes</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Munge-the-genomes">Munge the genomes<a class="anchor-link" href="#Munge-the-genomes">&#182;</a></h2><p>Not all the genomes are the same len. I am attempting to make them the same size as the ref genome, and adding a z
whenever i do any padding.</p>
<p>Eventually I would want to figure out a better way to align the genomes, or take the different sizes into account as that is prob significant.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">munged_genomes</span><span class="p">():</span>
    <span class="n">g</span> <span class="o">=</span> <span class="n">load_genomes</span><span class="p">()</span>
    <span class="n">ref_g</span> <span class="o">=</span> <span class="n">g</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

    <span class="n">munged_genomes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">genome</span> <span class="ow">in</span> <span class="n">g</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">genome</span><span class="p">)</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">ref_g</span><span class="p">):</span>
            <span class="c1"># Need to extend genome so len matches</span>
            <span class="n">m_genome</span> <span class="o">=</span> <span class="n">genome</span><span class="o">.</span><span class="n">ljust</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">ref_g</span><span class="p">),</span> <span class="s1">&#39;z&#39;</span><span class="p">)</span>
            <span class="n">munged_genomes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">m_genome</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">genome</span><span class="p">)</span> <span class="o">&gt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">ref_g</span><span class="p">):</span>
            <span class="n">munged_genomes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">genome</span><span class="p">[:</span><span class="nb">len</span><span class="p">(</span><span class="n">ref_g</span><span class="p">)])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">munged_genomes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">genome</span><span class="p">)</span>

    <span class="c1"># Sanity Check</span>
    <span class="n">l</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">ref_g</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">munged_genomes</span><span class="p">:</span>
        <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="o">==</span> <span class="n">l</span>

    <span class="k">return</span> <span class="n">munged_genomes</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Compute the munged genome sequences</span>
<span class="n">munged_genome_sequences</span> <span class="o">=</span> <span class="n">munged_genomes</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Using folder /Users/ddiaz/src/corona/generated/ to load genomes
Getting genome from file /Users/ddiaz/src/corona/generated/genBankRecord_MT044258.1.gb
Getting genome from file /Users/ddiaz/src/corona/generated/genBankRecord_MN988713.1.gb
Getting genome from file /Users/ddiaz/src/corona/generated/genBankRecord_MT027062.1.gb
Getting genome from file /Users/ddiaz/src/corona/generated/genBankRecord_MN908947.gb
Getting genome from file /Users/ddiaz/src/corona/generated/genBankRecord_MT077125.1.gb
Getting genome from file /Users/ddiaz/src/corona/generated/genBankRecord_MT039888.1.gb
Getting genome from file /Users/ddiaz/src/corona/generated/genBankRecord_MT019531.1.gb
Getting genome from file /Users/ddiaz/src/corona/generated/genBankRecord_MT039887.1.gb
Getting genome from file /Users/ddiaz/src/corona/generated/genBankRecord_MN985325.1.gb
Getting genome from file /Users/ddiaz/src/corona/generated/genBankRecord_MT093571.1.gb
Getting genome from file /Users/ddiaz/src/corona/generated/genBankRecord_LC534418.1.gb
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Set-up-functions-to-transform-the-genome-into-its-one-hot-encoded-form.">Set up functions to transform the genome into its one-hot encoded form.<a class="anchor-link" href="#Set-up-functions-to-transform-the-genome-into-its-one-hot-encoded-form.">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">######################################</span>
<span class="c1"># Setup One Hot Encoding Function</span>
<span class="c1">######################################</span>

<span class="c1"># One hot encode a DNA sequence string</span>
<span class="c1"># non &#39;acgt&#39; bases (n) are 0000</span>
<span class="c1"># returns a L x 4 numpy array</span>

<span class="n">label_encoder</span> <span class="o">=</span> <span class="n">LabelEncoder</span><span class="p">()</span>
<span class="c1"># z is also used when genomes are unequal in size.</span>
<span class="n">label_encoder</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="s1">&#39;a&#39;</span><span class="p">,</span><span class="s1">&#39;c&#39;</span><span class="p">,</span><span class="s1">&#39;g&#39;</span><span class="p">,</span><span class="s1">&#39;t&#39;</span><span class="p">,</span><span class="s1">&#39;z&#39;</span><span class="p">]))</span>

<span class="k">def</span> <span class="nf">string_to_array</span><span class="p">(</span><span class="n">my_string</span><span class="p">):</span>
    <span class="n">my_string</span> <span class="o">=</span> <span class="n">my_string</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
    <span class="n">my_string</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s1">&#39;[^acgt]&#39;</span><span class="p">,</span> <span class="s1">&#39;z&#39;</span><span class="p">,</span> <span class="n">my_string</span><span class="p">)</span>
    <span class="n">my_array</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">my_string</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">my_array</span>

<span class="k">def</span> <span class="nf">one_hot_encoder</span><span class="p">(</span><span class="n">my_array</span><span class="p">):</span>
    <span class="n">integer_encoded</span> <span class="o">=</span> <span class="n">label_encoder</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">my_array</span><span class="p">)</span>
    <span class="c1"># n_values is very important, it ensures all the ecoded genomes are nx5</span>
    <span class="c1"># note: n_values was deprecated, have to use categories instead</span>
    <span class="n">onehot_encoder</span> <span class="o">=</span> <span class="n">OneHotEncoder</span><span class="p">(</span><span class="n">sparse</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">int</span><span class="p">,</span> <span class="n">categories</span><span class="o">=</span><span class="p">[</span><span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">)])</span>
    <span class="n">integer_encoded</span> <span class="o">=</span> <span class="n">integer_encoded</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">integer_encoded</span><span class="p">),</span> <span class="mi">1</span><span class="p">)</span>
    <span class="n">onehot_encoded</span> <span class="o">=</span> <span class="n">onehot_encoder</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">integer_encoded</span><span class="p">)</span>
    <span class="n">onehot_encoded</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">onehot_encoded</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">onehot_encoded</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Test one hot encoder</span>
<span class="k">def</span> <span class="nf">test_one_hot_encoder</span><span class="p">():</span>
    <span class="n">test_sequence</span> <span class="o">=</span> <span class="s1">&#39;AACGCGGTTNN&#39;</span>
    <span class="n">test_sequence_hot</span> <span class="o">=</span> <span class="n">one_hot_encoder</span><span class="p">(</span><span class="n">string_to_array</span><span class="p">(</span><span class="n">test_sequence</span><span class="p">))</span>
    <span class="n">expected_sequence_hot</span> <span class="o">=</span>   <span class="p">[[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span>
                               <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span>
                               <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span>
                               <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span>
                               <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span>
                               <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span>
                               <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span>
                               <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span>
                               <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span>
                               <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span>
                               <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]]</span>

    <span class="c1"># Lets check this function is working as expected</span>
    <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">array_equal</span><span class="p">(</span><span class="n">test_sequence_hot</span><span class="p">,</span> <span class="n">expected_sequence_hot</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">test_one_hot_encoder</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="One-Hot-Encode-ref-genome.">One Hot Encode ref genome.<a class="anchor-link" href="#One-Hot-Encode-ref-genome.">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># r = ref_genome_seq[0:5]</span>
<span class="n">ref_seq_hot</span> <span class="o">=</span> <span class="n">one_hot_encoder</span><span class="p">(</span><span class="n">string_to_array</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">load_ref_genome</span><span class="p">())))</span>

<span class="c1"># DEV Note: Because there are no unknown letters in the ref genome, the output hot encoding is only 3 positions instead of</span>
<span class="c1"># 4 like in the test above.</span>
<span class="c1"># We can force this to be 4, by updating the one hot encoding function to take in a categories variable, which is what we have done.</span>
<span class="c1"># print(ref_seq_hot)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Quick-note:">Quick note:<a class="anchor-link" href="#Quick-note:">&#182;</a></h4><p>Notice then above array is only 3 bits</p>
<div class="highlight"><pre><span></span>[1 0 0]
A 1 in the first position means A.
A 1 in the second position means C.
A 1 in the third position means G.
And all zeros means T
</pre></div>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Let's-create-a-generic-function-that-does-the-genome-load-and-one-hot-encoding">Let's create a generic function that does the genome load and one hot encoding<a class="anchor-link" href="#Let's-create-a-generic-function-that-does-the-genome-load-and-one-hot-encoding">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">get_one_hot_genome_encoding</span><span class="p">(</span><span class="n">munged_genome_sequence</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    :returns A one hot encode genome</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">genome_seq</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">munged_genome_sequence</span><span class="p">)</span>
    <span class="n">seq_hot</span> <span class="o">=</span> <span class="n">one_hot_encoder</span><span class="p">(</span><span class="n">string_to_array</span><span class="p">(</span><span class="n">genome_seq</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">seq_hot</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Lets-get-all-the-one-hot-encodings-for-the-gb-files-we-have">Lets get all the one hot encodings for the gb files we have<a class="anchor-link" href="#Lets-get-all-the-one-hot-encodings-for-the-gb-files-we-have">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">get_one_hot_genome_encodings</span><span class="p">(</span><span class="n">munged_genome_sequences</span><span class="p">):</span>
    <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">genome</span> <span class="ow">in</span> <span class="n">munged_genome_sequences</span><span class="p">:</span>
        <span class="n">r</span> <span class="o">=</span> <span class="n">get_one_hot_genome_encoding</span><span class="p">(</span><span class="n">genome</span><span class="p">)</span>
        <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">r</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">result</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">one_hot_encoded_genomes</span> <span class="o">=</span> <span class="n">get_one_hot_genome_encodings</span><span class="p">(</span><span class="n">munged_genome_sequences</span><span class="p">)</span>

<span class="c1"># print(&quot;Array of one hot encoded genomes&quot;)</span>
<span class="c1"># print(one_hot_encoded_genomes)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Next-step-is-to-try-and-generate-the-mutation-diagram">Next step is to try and generate the mutation diagram<a class="anchor-link" href="#Next-step-is-to-try-and-generate-the-mutation-diagram">&#182;</a></h2><ul>
<li>Each row will be an different seq.</li>
<li>Below is a test mutation diagram.</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># ACG</span>
<span class="n">g1_ref</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],[</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">]]</span>
<span class="c1"># ACG</span>
<span class="n">g2</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],[</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">]]</span>
<span class="c1"># ACT</span>
<span class="c1"># This one has a mutation in the 3rd letter</span>
<span class="n">g3</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],[</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">]]</span>

<span class="c1"># Two options, we can either compare to the ref genome, or compare to an array that represents</span>
<span class="c1"># the most common letter in that position</span>

<span class="c1"># Lets start with the former, then move to the latter</span>
<span class="c1"># A final zero bit (black) will be ref genome</span>
<span class="c1"># A one (white) will be mutation from ref genome</span>

<span class="c1"># X = np.random.random((100, 100)) # sample 2D array</span>
<span class="c1"># plt.imshow(X, cmap=&quot;gray&quot;)</span>
<span class="c1"># plt.show()</span>

<span class="c1"># this is our basline, all zeros</span>
<span class="n">genome_chart</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">0</span><span class="p">]</span><span class="o">*</span><span class="nb">len</span><span class="p">(</span><span class="n">g1_ref</span><span class="p">)]</span>
<span class="c1"># print(genome_chart)</span>

<span class="k">def</span> <span class="nf">compare</span><span class="p">(</span><span class="n">ref_genome</span><span class="p">,</span> <span class="n">new_genome</span><span class="p">):</span>
    <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">ref_genome</span><span class="p">)):</span>
        <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">array_equal</span><span class="p">(</span><span class="n">ref_genome</span><span class="p">[</span><span class="n">i</span><span class="p">],</span> <span class="n">new_genome</span><span class="p">[</span><span class="n">i</span><span class="p">]):</span>
            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">result</span>

<span class="n">result1</span> <span class="o">=</span> <span class="n">compare</span><span class="p">(</span><span class="n">g1_ref</span><span class="p">,</span><span class="n">g2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result1</span><span class="p">)</span>
<span class="n">result2</span> <span class="o">=</span> <span class="n">compare</span><span class="p">(</span><span class="n">g1_ref</span><span class="p">,</span><span class="n">g3</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result2</span><span class="p">)</span>
<span class="n">genome_chart</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result1</span><span class="p">)</span>
<span class="n">genome_chart</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">genome_chart</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">genome_chart</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s2">&quot;gray&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[0, 0, 0]
[0, 0, 1]
[[0, 0, 0], [0, 0, 0], [0, 0, 1]]
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Ok-let's-pause.">Ok let's pause.<a class="anchor-link" href="#Ok-let's-pause.">&#182;</a></h2><p>Above we created 3 sample genomes that were only 3 letters long. one was the ref genome.
Only one genome had a mutation in the last position.
So if we compare that to the chart, the top row is the ref genome, its all black becuase its the ref.
THe bottom row is the mutated genome, with the last column, last row being white as thats were the mutation is.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Now lets do the same thing to the 3 genomes we have.</span>
<span class="n">g1</span> <span class="o">=</span> <span class="n">ref_seq_hot</span>
<span class="n">gN</span> <span class="o">=</span> <span class="n">one_hot_encoded_genomes</span>
<span class="c1"># imchart requires floats</span>
<span class="n">genome_chart</span> <span class="o">=</span> <span class="p">[[</span><span class="nb">float</span><span class="p">(</span><span class="mi">0</span><span class="p">)]</span><span class="o">*</span><span class="nb">len</span><span class="p">(</span><span class="n">g1</span><span class="p">)]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">compare_with_fudging</span><span class="p">(</span><span class="n">ref_genome</span><span class="p">,</span> <span class="n">new_genome</span><span class="p">):</span>
    <span class="c1"># TODO: this func shouldnt be needed anymore cause we did some munging earlier</span>
    <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">ref_genome</span><span class="p">)):</span>
        <span class="c1"># check if arrays are equal, if not write a 1</span>
        <span class="c1"># sometimes arrays arent equal. for now, lets just assume thats a mutation</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">array_equal</span><span class="p">(</span><span class="n">ref_genome</span><span class="p">[</span><span class="n">i</span><span class="p">],</span> <span class="n">new_genome</span><span class="p">[</span><span class="n">i</span><span class="p">]):</span>
                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="mi">0</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">IndexError</span><span class="p">:</span>
            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="mi">1</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="mi">1</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">result</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">genome</span> <span class="ow">in</span> <span class="n">gN</span><span class="p">[:]:</span>
    <span class="n">c</span> <span class="o">=</span> <span class="n">compare_with_fudging</span><span class="p">(</span><span class="n">g1</span><span class="p">,</span><span class="n">genome</span><span class="p">)</span>
    <span class="n">genome_chart</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>

<span class="c1"># for some reason i am getting a type error when i do the full array, for now , lets justt do a partial.</span>
<span class="c1"># genome_chart_debug = [genome_chart[0][:500], genome_chart[1][:500], genome_chart[2][:500]]</span>
<span class="n">genome_chart_debug</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">arr</span> <span class="ow">in</span> <span class="n">genome_chart</span><span class="p">:</span>
    <span class="n">genome_chart_debug</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">arr</span><span class="p">[</span><span class="mi">250</span><span class="p">:</span><span class="mi">300</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Plot-the-genome-mutation-matrix">Plot the genome mutation matrix<a class="anchor-link" href="#Plot-the-genome-mutation-matrix">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># plt.figure(figsize = (15,5))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">real</span><span class="p">(</span><span class="n">genome_chart_debug</span><span class="p">),</span> <span class="n">cmap</span><span class="o">=</span><span class="s2">&quot;gray&quot;</span><span class="p">,</span> <span class="n">interpolation</span><span class="o">=</span><span class="s2">&quot;nearest&quot;</span><span class="p">,</span> <span class="n">aspect</span><span class="o">=</span><span class="s1">&#39;auto&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Results">Results<a class="anchor-link" href="#Results">&#182;</a></h2><p>Above you will see 50 base pairs (Position 250-&gt;300). The black bar at the top being the ref genome, and the white lines representing mutations.</p>
<h2 id="What-can-be-improved">What can be improved<a class="anchor-link" href="#What-can-be-improved">&#182;</a></h2><ul>
<li>Right now I am only using a few genomes, and only a subset of the genome, so the chart still looks funky, and is not the checkerboard I was expecting.</li>
<li>Also, I did not take into consideration actually aligning the genome.</li>
<li>I also added some fudge factor for unequal genome lengths.</li>
<li>Everything is being compared against the ref genome. It would probably be more interesting to derive the most common letter for that position, then label one wild, and one mutation.</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Useful-Links:">Useful Links:<a class="anchor-link" href="#Useful-Links:">&#182;</a></h2><p><a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc132">http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc132</a>
<a href="https://www.kaggle.com/thomasnelson/working-with-dna-sequence-data-for-ml">https://www.kaggle.com/thomasnelson/working-with-dna-sequence-data-for-ml</a></p>

</div>
</div>
</div>
 


{{< /rawhtml >}}


