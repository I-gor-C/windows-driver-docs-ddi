---
UID: NF.wiautil.wiauStrC2W
title: wiauStrC2W
author: windows-driver-content
description: The wiauStrC2W function converts an ANSI character string to a Unicode string.
old-location: image\wiaustrc2w.htm
old-project: image
ms.assetid: 66d90248-c496-44c8-98f4-5eb3e2cae130
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: wiauStrC2W
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiautil.h
req.include-header: Wiautil.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiauStrC2W
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
req.iface: 
req.product: Windows 10 or later.
---

# wiauStrC2W function



## -description
<p>The <b>wiauStrC2W</b> function converts an ANSI character string to a Unicode string.</p>


## -syntax

````
HRESULT _stdcall wiauStrC2W(
  _In_  CHAR  *pszSrc,
  _Out_ WCHAR *pwszDst,
        INT   iSize
);
````


## -parameters
<dl>

### -param pszSrc [in]

<dd>
<p>Points to the ANSI string to convert.</p>
</dd>

### -param pwszDst [out]

<dd>
<p>Pointer to a memory location that receives the converted Unicode string.</p>
</dd>

### -param iSize 

<dd>
<p>Specifies the size, in bytes, of the buffer pointed to by <i>pwszDst</i>.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error.</p>

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
<dt>Wiautil.h (include Wiautil.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wiautil\nf-wiautil-wiaustrc2c.md">wiauStrC2C</a>
</dt>
<dt>
<a href="..\wiautil\nf-wiautil-wiaustrw2c.md">wiauStrW2C</a>
</dt>
<dt>
<a href="..\wiautil\nf-wiautil-wiaustrw2w.md">wiauStrW2W</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiauStrC2W function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
