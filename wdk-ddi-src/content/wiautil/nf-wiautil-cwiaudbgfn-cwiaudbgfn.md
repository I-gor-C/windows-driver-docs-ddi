---
UID: NF.wiautil.CWiauDbgFn.CWiauDbgFn
title: CWiauDbgFn::CWiauDbgFn
author: windows-driver-content
description: The CWiauDbgFn::CWiauDbgFn method is used for tracing when a function or method is entered.
old-location: image\cwiaudbgfn_cwiaudbgfn.htm
ms.assetid: dbb367a7-d7e6-4081-9618-1c4e38cccd31
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiautil.h
req.include-header: Wiautil.h, Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CWiauDbgFn.CWiauDbgFn
req.alt-loc: Wiautil.h
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
ms.keywords: CWiauDbgFn, CWiauDbgFn, CWiauDbgFn::CWiauDbgFn
req.iface: CWiauDbgFn
req.product: Windows 10 or later.
---

# CWiauDbgFn::CWiauDbgFn method



## -description
<p>The <b>CWiauDbgFn::CWiauDbgFn</b> method is used for tracing when a function or method is entered.</p>


## -syntax

````
void CWiauDbgFn(
   LPCSTR   fname
);
````


## -parameters
<dl>

### -param <i>fname</i> 

<dd>
<p>Specifies the name of the function or method being entered.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiautil.h (include Wiautil.h or Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540356">CWiauDbgFn::~CWiauDbgFn</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20CWiauDbgFn::CWiauDbgFn method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
