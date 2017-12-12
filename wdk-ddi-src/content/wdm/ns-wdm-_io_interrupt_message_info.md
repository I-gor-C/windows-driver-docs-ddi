---
UID: NS.WDM._IO_INTERRUPT_MESSAGE_INFO
title: _IO_INTERRUPT_MESSAGE_INFO
author: windows-driver-content
description: The IO_INTERRUPT_MESSAGE_INFO structure describes the driver's message-signaled interrupts.
old-location: kernel\io_interrupt_message_info.htm
old-project: kernel
ms.assetid: d740d55e-6549-494d-9b2a-39d5c2e670d3
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _IO_INTERRUPT_MESSAGE_INFO, *PIO_INTERRUPT_MESSAGE_INFO, IO_INTERRUPT_MESSAGE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IO_INTERRUPT_MESSAGE_INFO
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.product: Windows 10 or later.
---

# _IO_INTERRUPT_MESSAGE_INFO structure



## -description
The <b>IO_INTERRUPT_MESSAGE_INFO</b> structure describes the driver's message-signaled interrupts.



## -syntax

````
typedef struct _IO_INTERRUPT_MESSAGE_INFO {
  KIRQL                           UnifiedIrql;
  ULONG                           MessageCount;
  IO_INTERRUPT_MESSAGE_INFO_ENTRY MessageInfo[1];
} IO_INTERRUPT_MESSAGE_INFO, *PIO_INTERRUPT_MESSAGE_INFO;
````


## -struct-fields

### -field UnifiedIrql

Specifies the IRQL at which the driver's <a href="kernel.interruptmessageservice">InterruptMessageService</a> routine runs. If the driver specified an interrupt spin lock for its interrupts, <b>UnifiedIrql</b> also specifies the IRQL at which the interrupt spin lock is acquired. 


### -field MessageCount

Specifies the number of message-signaled interrupts allocated for the driver.


### -field MessageInfo

Variable-length array that specifies an <a href="kernel.io_interrupt_message_info_entry">IO_INTERRUPT_MESSAGE_INFO_ENTRY</a> structure for each message-signaled interrupt allocated for the driver. The <b>MessageCount</b> member specifies the number of entries in this array. 


## -remarks
When a driver calls <a href="kernel.ioconnectinterruptex">IoConnectInterruptEx</a> to register an <a href="kernel.interruptmessageservice">InterruptMessageService</a> routine, <b>IoConnectInterruptEx</b> provides a pointer to <b>IO_INTERRUPT_MESSAGE_INFO</b> in <i>Parameters</i>-&gt;<b>MessageBased.ConnectionContext</b>. For more information, see <a href="kernel.io_connect_interrupt_parameters">IO_CONNECT_INTERRUPT_PARAMETERS</a>.


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.io_connect_interrupt_parameters">IO_CONNECT_INTERRUPT_PARAMETERS</a>
</dt>
<dt>
<a href="kernel.io_interrupt_message_info_entry">IO_INTERRUPT_MESSAGE_INFO_ENTRY</a>
</dt>
<dt>
<a href="kernel.ioconnectinterruptex">IoConnectInterruptEx</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IO_INTERRUPT_MESSAGE_INFO structure%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

