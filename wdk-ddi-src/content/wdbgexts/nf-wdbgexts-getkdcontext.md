---
UID: NF.wdbgexts.GetKdContext
title: GetKdContext macro
author: windows-driver-content
description: The GetKdContext function returns the total number of processors and the number of the current processor in the structure ppi points to.
old-location: debugger\getkdcontext.htm
old-project: Debugger
ms.assetid: cf795629-cf62-45fa-ad5e-e2eef576bcfd
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: GetKdContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetKdContext
req.alt-loc: wdbgexts.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# GetKdContext macro



## -description
The <b>GetKdContext</b> function returns the total number of processors and the number of the current processor in the structure <i>ppi</i> points to.



## -syntax

````
ULONG GetKdContext(
   PPROCESSORINFO ppi
);
````


## -parameters

### -param ppi 

Points to the following structure:

<pre class="syntax" xml:space="preserve"><code>typedef struct _tagPROCESSORINFO {
  USHORT  Processor;           // current processor
  USHORT  NumberProcessors;    // total number of processors
} PROCESSORINFO, *PPROCESSORINFO;</code></pre>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdbgexts.h (include Wdbgexts.h or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>