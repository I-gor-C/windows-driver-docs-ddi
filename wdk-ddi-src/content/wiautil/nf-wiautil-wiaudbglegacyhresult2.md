---
UID: NF.wiautil.wiauDbgLegacyHresult2
title: wiauDbgLegacyHresult2
author: windows-driver-content
description: The wiauDbgLegacyHresult2 function logs a default message containing an HRESULT.
old-location: image\wiaudbglegacyhresult2.htm
ms.assetid: 1b73c94b-07a8-4b65-8ed7-d5f1a073c3b2
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiautil.h
req.include-header: Wiautil.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiauDbgLegacyHresult2
req.alt-loc: wiautil.h
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
ms.keywords: wiauDbgLegacyHresult2
req.iface: 
req.product: Windows 10 or later.
---

# wiauDbgLegacyHresult2 function



## -description
<p>The <b>wiauDbgLegacyHresult2</b> function logs a default message containing an HRESULT.</p>


## -syntax

````
inline void __stdcall wiauDbgLegacyHresult2(
  _In_ HINSTANCE hInstance,
       HRESULT   hr
);
````


## -parameters
<dl>

### -param <i>hInstance</i> [in]

<dd>
<p>Specifies the handle to the DLL instance.</p>
</dd>

### -param <i>hr</i> 

<dd>
<p>Specifies the HRESULT to be logged.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A call to the <b>wiauDbgLegacyHresult2</b> function is equivalent to the following call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549637">wiauDbgErrorHr</a> function:</p>

<p>That is, only one line is output to the log file and/or debugger. The line has the following form:</p>

<p>A call to the <b>wiauDbgLegacyHresult2</b> function is equivalent to the following call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549637">wiauDbgErrorHr</a> function:</p>

<p>That is, only one line is output to the log file and/or debugger. The line has the following form:</p>

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
<dt>Wiautil.h (include Wiautil.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549637">wiauDbgErrorHr</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiauDbgLegacyHresult2 function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
