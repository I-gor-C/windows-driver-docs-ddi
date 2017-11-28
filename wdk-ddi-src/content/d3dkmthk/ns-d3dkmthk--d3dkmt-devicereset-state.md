---
UID: NS.d3dkmthk._D3DKMT_DEVICERESET_STATE
title: D3DKMT_DEVICERESET_STATE
author: windows-driver-content
description: The D3DKMT_DEVICERESET_STATE structure identifies reset status.
old-location: display\d3dkmt_devicereset_state.htm
old-project: display
ms.assetid: c2037d77-8745-4307-ac12-54f62f20c2d9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_DEVICERESET_STATE, D3DKMT_DEVICERESET_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_DEVICERESET_STATE
req.alt-loc: d3dkmthk.h
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

# D3DKMT_DEVICERESET_STATE structure



## -description
<p>The D3DKMT_DEVICERESET_STATE structure identifies reset status.</p>


## -syntax

````
typedef struct _D3DKMT_DEVICERESET_STATE {
  union {
    struct {
      UINT DesktopSwitched  :1;
      UINT Reserved  :31;
    };
    UINT   Value;
  };
} D3DKMT_DEVICERESET_STATE;
````


## -struct-fields
<dl>

### -field <b>DesktopSwitched</b>

<dd>
<p>A UINT value that specifies whether the desktop that the calling process is created on switched from being visible to being invisible. For example, when the security screen appears because a user pressed CTRL+ALT+DEL, the desktop that the calling process is created on becomes invisible. </p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 31 bits (0xFFFFFFFE) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A 32-bit value that identifies reset status.</p>
</dd>
</dl>

## -remarks


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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548030">D3DKMT_GETDEVICESTATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_DEVICERESET_STATE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
