---
UID: NS.d3dumddi._D3DDDIARG_GETCAPS
title: D3DDDIARG_GETCAPS
author: windows-driver-content
description: The D3DDDIARG_GETCAPS structure contains display device capabilities of a particular type.
old-location: display\d3dddiarg_getcaps.htm
ms.assetid: 50063bd0-c9d4-4013-8f83-8f9d92aa87c0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_GETCAPS
req.alt-loc: d3dumddi.h
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
ms.keywords: D3DDDIARG_GETCAPS, D3DDDIARG_GETCAPS
req.iface: 
---

# D3DDDIARG_GETCAPS structure



## -description
<p>The D3DDDIARG_GETCAPS structure contains display device capabilities of a particular type.</p>


## -syntax

````
typedef struct _D3DDDIARG_GETCAPS {
  D3DDDICAPS_TYPE Type;
  VOID            *pInfo;
  VOID            *pData;
  UINT            DataSize;
} D3DDDIARG_GETCAPS;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>[in] The type of capabilities to retrieve. The Microsoft Direct3D runtime can supply one of the values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a> enumeration type, possibly along with information in the buffer that is pointed to by <b>pInfo</b>, to retrieve particular capability data in the buffer at <b>pData</b>.</p>
</dd>

### -field <b>pInfo</b>

<dd>
<p>[in] A pointer to a buffer that contains data that specifies the specific condition on which to retrieve the capabilities of the type that is specified by the <b>Type</b> member.</p>
</dd>

### -field <b>pData</b>

<dd>
<p>[out] A pointer to a buffer that is filled with capabilities of the type that is specified by the <b>Type</b> member and possibly determined by the condition that is specified in the buffer at <b>pInfo</b>.</p>
</dd>

### -field <b>DataSize</b>

<dd>
<p>[in/out] The size, in bytes, of the buffer at <b>pData</b>.</p>
</dd>
</dl>

## -remarks
<p>For information on how to specify <b>D3DDDIARG_GETCAPS</b> member values along with <a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a> constant values, see Remarks of <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_GETCAPS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
