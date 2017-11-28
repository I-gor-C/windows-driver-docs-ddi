---
UID: NE.d3dkmthk._D3DKMT_DEVICEEXECUTION_STATE
title: D3DKMT_DEVICEEXECUTION_STATE
author: windows-driver-content
description: Contains values that indicate the execution status for a device.
old-location: display\d3dkmt_deviceexecution_state.htm
old-project: display
ms.assetid: 31935433-6fa4-4d1a-9ad4-879353102e71
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_DEVICEEXECUTION_STATE
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

# D3DKMT_DEVICEEXECUTION_STATE enumeration



## -description
<p>The <b>D3DKMT_DEVICEEXECUTION_STATE</b> enumeration type contains values that indicate the execution status for a device.</p>


## -syntax

````
typedef enum _D3DKMT_DEVICEEXECUTION_STATE { 
  D3DKMT_DEVICEEXECUTION_ACTIVE              = 1,
  D3DKMT_DEVICEEXECUTION_RESET               = 2,
  D3DKMT_DEVICEEXECUTION_HUNG                = 3,
  D3DKMT_DEVICEEXECUTION_STOPPED             = 4,
  D3DKMT_DEVICEEXECUTION_ERROR_OUTOFMEMORY   = 5,
  D3DKMT_DEVICEEXECUTION_ERROR_DMAFAULT      = 6,
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
  D3DKMT_DEVICEEXECUTION_ERROR_DMAPAGEFAULT  = 7,
#endif 
  
} D3DKMT_DEVICEEXECUTION_STATE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMT_DEVICEEXECUTION_ACTIVE"></a><a id="d3dkmt_deviceexecution_active"></a><b>D3DKMT_DEVICEEXECUTION_ACTIVE</b>

<dd>
<p>The device is actively executing.</p>
</dd>

### -field <a id="D3DKMT_DEVICEEXECUTION_RESET"></a><a id="d3dkmt_deviceexecution_reset"></a><b>D3DKMT_DEVICEEXECUTION_RESET</b>

<dd>
<p>The device is reset.</p>
</dd>

### -field <a id="D3DKMT_DEVICEEXECUTION_HUNG"></a><a id="d3dkmt_deviceexecution_hung"></a><b>D3DKMT_DEVICEEXECUTION_HUNG</b>

<dd>
<p>The device is hung. The device is unable to continue.</p>
</dd>

### -field <a id="D3DKMT_DEVICEEXECUTION_STOPPED"></a><a id="d3dkmt_deviceexecution_stopped"></a><b>D3DKMT_DEVICEEXECUTION_STOPPED</b>

<dd>
<p>
      The device is stopped.
     </p>
</dd>

### -field <a id="D3DKMT_DEVICEEXECUTION_ERROR_OUTOFMEMORY"></a><a id="d3dkmt_deviceexecution_error_outofmemory"></a><b>D3DKMT_DEVICEEXECUTION_ERROR_OUTOFMEMORY</b>

<dd>
<p>Even after the video memory manager split the DMA buffer, the video memory manager could not page-in all of the required allocations into video memory at the same time. The device is unable to continue.</p>
</dd>

### -field <a id="D3DKMT_DEVICEEXECUTION_ERROR_DMAFAULT"></a><a id="d3dkmt_deviceexecution_error_dmafault"></a><b>D3DKMT_DEVICEEXECUTION_ERROR_DMAFAULT</b>

<dd>
<p>The display miniport driver reported a fault while processing a DMA buffer for the device. The device is unable to continue.</p>
</dd>

### -field <a id="D3DKMT_DEVICEEXECUTION_ERROR_DMAPAGEFAULT"></a><a id="d3dkmt_deviceexecution_error_dmapagefault"></a><b>D3DKMT_DEVICEEXECUTION_ERROR_DMAPAGEFAULT</b>

<dd>
<p>The display miniport driver reported a page fault while processing a DMA buffer for the device. The device is unable to continue.</p>
</dd>

### -field <a id=""></a><b></b>

<dd></dd>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_DEVICEEXECUTION_STATE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
