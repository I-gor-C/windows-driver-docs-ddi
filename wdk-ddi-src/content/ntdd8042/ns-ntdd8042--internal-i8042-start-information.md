---
UID: NS.ntdd8042._INTERNAL_I8042_START_INFORMATION
title: INTERNAL_I8042_START_INFORMATION
author: windows-driver-content
description: INTERNAL_I8042_START_INFORMATION specifies the interrupt object that an optional, vendor-supplied, upper-level filter device driver can use to synchronize its operation with an I8042prt ISR.
old-location: hid\internal_i8042_start_information.htm
old-project: hid
ms.assetid: 8ceaa9de-195f-4a89-bc3e-323256097248
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: INTERNAL_I8042_START_INFORMATION, INTERNAL_I8042_START_INFORMATION, *PINTERNAL_I8042_START_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdd8042.h
req.include-header: Ntdd8042.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: INTERNAL_I8042_START_INFORMATION
req.alt-loc: ntdd8042.h
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

# INTERNAL_I8042_START_INFORMATION structure



## -description
<p>INTERNAL_I8042_START_INFORMATION specifies the <a href="wdkgloss.i#wdkgloss.interrupt_object#wdkgloss.interrupt_object"><i>interrupt object</i></a> that an optional, vendor-supplied, upper-level filter device driver can use to synchronize its operation with an I8042prt ISR. </p>


## -syntax

````
typedef struct _INTERNAL_I8042_START_INFORMATION {
  ULONG       Size;
  PKINTERRUPT InterruptObject;
  ULONG       Reserved[8];
} INTERNAL_I8042_START_INFORMATION, *PINTERNAL_I8042_START_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size, in bytes, of an INTERNAL_I8042_START_INFORMATION structure.</p>
</dd>

### -field <b>InterruptObject</b>

<dd>
<p>Pointer to an interrupt object. I8042prt supplies the interrupt object.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks
<p>This structure is used with <a href="https://msdn.microsoft.com/library/windows/hardware/ff541257">IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff541265">IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION</a> requests.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdd8042.h (include Ntdd8042.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541257">IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541265">IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20INTERNAL_I8042_START_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
