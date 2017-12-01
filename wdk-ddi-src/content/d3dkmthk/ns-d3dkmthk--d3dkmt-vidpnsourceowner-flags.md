---
UID: NS.d3dkmthk._D3DKMT_VIDPNSOURCEOWNER_FLAGS
title: D3DKMT_VIDPNSOURCEOWNER_FLAGS
author: windows-driver-content
description: Specifies output duplication options for use with the D3DKMTSetVidPnSourceOwner1 function.
old-location: display\d3dkmt_vidpnsourceowner_flags.htm
old-project: display
ms.assetid: acc4e9d9-235f-4605-ae51-5056108843dc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_VIDPNSOURCEOWNER_FLAGS, D3DKMT_VIDPNSOURCEOWNER_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_VIDPNSOURCEOWNER_FLAGS
req.alt-loc: D3dkmthk.h
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
---

# D3DKMT_VIDPNSOURCEOWNER_FLAGS structure



## -description
<p>Specifies output duplication options for use with the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtsetvidpnsourceowner1.md">D3DKMTSetVidPnSourceOwner1</a> function.</p>


## -syntax

````
typedef struct _D3DKMT_VIDPNSOURCEOWNER_FLAGS {
  union {
    struct {
      UINT AllowOutputDuplication  :1;
      UINT Reserved  :31;
    };
    UINT   Value;
  };
} D3DKMT_VIDPNSOURCEOWNER_FLAGS;
````


## -struct-fields
<dl>

### -field <b>AllowOutputDuplication</b>

<dd>
<p>If a value of one, the video present network (VidPN) explicitly allows output duplication. Otherwise output duplication is not allowed.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>Specifies the number of output duplication paths on the VidPN.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtsetvidpnsourceowner1.md">D3DKMTSetVidPnSourceOwner1</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_VIDPNSOURCEOWNER_FLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
