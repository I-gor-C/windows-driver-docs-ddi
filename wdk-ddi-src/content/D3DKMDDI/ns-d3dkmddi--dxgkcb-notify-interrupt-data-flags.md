---
UID: NS.d3dkmddi._DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS
title: DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS
author: windows-driver-content
description: The DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS structure indicates whether the display miniport driver provides a physical adapter mask in a call to the DxgkCbNotifyInterrupt function.
old-location: display\dxgkcb_notify_interrupt_data_flags.htm
ms.assetid: 69554ec0-3d5e-4a53-8b45-2f821ddbfd3c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS, DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS
req.iface: 
---

# DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS structure



## -description
<p>The DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS structure indicates whether the display miniport driver provides a physical adapter mask in a call to the <a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a> function.</p>


## -syntax

````
typedef struct _DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS {
  union {
    struct {
      UINT ValidPhysicalAdapterMask  :1;
      UINT HsyncFlipCompletion  :1;
      UINT Reserved  :30;
    };
    UINT Value;
  };
} DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS;
````


## -struct-fields
<dl>

### -field <b>ValidPhysicalAdapterMask</b>

<dd>
<p>A UINT value that specifies whether the driver provides a physical adapter mask. If this member is set, the driver provides a physical adapter mask in the <b>PhysicalAdapterMask</b> member of the <b>CrtcVsync</b> structure that is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557538">DXGKARGCB_NOTIFY_INTERRUPT_DATA</a> structure. </p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>HsyncFlipCompletion</b>

<dd>
<p>A UINT value that specifies whether the Hsync flip has been completed.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 31 bits (0xFFFFFFFE) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A member in the union that DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS contains that can hold a 32-bit value.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557538">DXGKARGCB_NOTIFY_INTERRUPT_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
