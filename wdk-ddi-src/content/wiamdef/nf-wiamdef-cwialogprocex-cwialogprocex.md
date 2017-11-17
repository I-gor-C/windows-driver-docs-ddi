---
UID: NF.wiamdef.CWiaLogProcEx.CWiaLogProcEx
title: CWiaLogProcEx::CWiaLogProcEx
author: windows-driver-content
description: The CWiaLogProcEx constructor is called when the function or method being logged is entered.
old-location: image\cwialogprocex_cwialogprocex.htm
ms.assetid: D4004501-2DA5-416C-A29B-C0084CF34DC9
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiamdef.h
req.include-header: Wiamdef.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CWiaLogProcEx.CWiaLogProcEx
req.alt-loc: Wiamdef.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
ms.keywords: CWiaLogProcEx, CWiaLogProcEx, CWiaLogProcEx::CWiaLogProcEx
req.iface: CWiaLogProcEx
req.product: Windows 10 or later.
---

# CWiaLogProcEx::CWiaLogProcEx method



## -description
<p>The <a href="https://msdn.microsoft.com/5DD3EC13-5DDD-4640-A841-00576F74429A">CWiaLogProcEx</a> constructor is called when the function or method being logged is entered.</p>


## -syntax

````
void CWiaLogProcEx(
   IWiaLogEx *pIWiaLogEx,
   INT       ResourceID,
   INT       DetailLevel,
   CHAR      *pszMsg,
   LONG      lMethodId = 0
);
````


## -parameters
<dl>

### -param <i>*pIWiaLogEx</i> 

<dd>
<p>Defines the <b>IWiaLogEx</b> parameter <i>*pIWiaLog</i>.</p>
</dd>

### -param <i>ResourceID</i> 

<dd>
<p>Defines the <b>INT</b> parameter <i>ResourceID</i>.</p>
</dd>

### -param <i>DetailLevel</i> 

<dd>
<p>Defines the <b>INT</b> parameter <i>DetailLevel</i>.</p>
</dd>

### -param <i>*pszMsg</i> 

<dd>
<p>Defines the <b>CHAR</b> parameter <i>*pszMsg</i>.</p>
</dd>

### -param <i>lMethodId = 0</i> 

<dd>
<p>Defines the <b>LONG</b> parameter <i>lMethodId</i>.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamdef.h (include Wiamdef.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.cwialogprocex">CWiaLogProcEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20CWiaLogProcEx::CWiaLogProcEx method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
