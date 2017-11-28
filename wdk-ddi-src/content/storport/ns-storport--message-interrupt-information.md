---
UID: NS.storport._MESSAGE_INTERRUPT_INFORMATION
title: MESSAGE_INTERRUPT_INFORMATION
author: windows-driver-content
description: The MESSAGE_INTERRUPT_INFORMATION structure describes a message signaled interrupt (MSI).
old-location: storage\message_interrupt_information.htm
old-project: storage
ms.assetid: 469896b3-3ae0-4edd-9fb0-ee5869633872
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MESSAGE_INTERRUPT_INFORMATION, MESSAGE_INTERRUPT_INFORMATION, *PMESSAGE_INTERRUPT_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MESSAGE_INTERRUPT_INFORMATION
req.alt-loc: storport.h
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

# MESSAGE_INTERRUPT_INFORMATION structure



## -description
<p>The <b>MESSAGE_INTERRUPT_INFORMATION</b> structure describes a message signaled interrupt (MSI).</p>


## -syntax

````
typedef struct _MESSAGE_INTERRUPT_INFORMATION {
  ULONG                 MessageId;
  ULONG                 MessageData;
  STOR_PHYSICAL_ADDRESS MessageAddress;
  ULONG                 InterruptVector;
  ULONG                 InterruptLevel;
  KINTERRUPT_MODE       InterruptMode;
} MESSAGE_INTERRUPT_INFORMATION, *PMESSAGE_INTERRUPT_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>MessageId</b>

<dd>
<p>An identifier identifies the MSI interrupt. A miniport driver can pass this value to <a href="https://msdn.microsoft.com/library/windows/hardware/ff567023">StorPortAcquireMSISpinLock</a> in the <i>MessageId</i> parameter to obtain a spin lock for synchronization purposes. </p>
</dd>

### -field <b>MessageData</b>

<dd>
<p>The data associated with the message. </p>
</dd>

### -field <b>MessageAddress</b>

<dd>
<p>The physical address associated with the message. </p>
</dd>

### -field <b>InterruptVector</b>

<dd>
<p>The interrupt vector associated with the message. </p>
</dd>

### -field <b>InterruptLevel</b>

<dd>
<p>The interrupt level associated with the message. </p>
</dd>

### -field <b>InterruptMode</b>

<dd>
<p>A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff554239">KINTERRUPT_MODE</a> that specifies the interrupt mode associated with the message.  </p>
</dd>
</dl>

## -remarks
<p>Miniport drivers retrieve the MSI information in a <b>MESSAGE_INTERRUPT_INFORMATION</b> structure by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567090">StorPortGetMSIInfo</a> routine. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567090">StorPortGetMSIInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MESSAGE_INTERRUPT_INFORMATION structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
