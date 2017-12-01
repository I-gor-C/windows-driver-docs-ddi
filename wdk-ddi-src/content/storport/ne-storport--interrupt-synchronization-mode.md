---
UID: NE.storport._INTERRUPT_SYNCHRONIZATION_MODE
title: INTERRUPT_SYNCHRONIZATION_MODE
author: windows-driver-content
description: The INTERRUPT_SYNCHRONIZATION_MODE enumerator specifies the interrupt synchronization mode.
old-location: storage\interrupt_synchronization_mode.htm
old-project: storage
ms.assetid: 964009ab-5f90-4f23-b22a-4c3e03d2449e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: storport.h
req.include-header: Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: INTERRUPT_SYNCHRONIZATION_MODE
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

# INTERRUPT_SYNCHRONIZATION_MODE enumeration



## -description
<p>The INTERRUPT_SYNCHRONIZATION_MODE enumerator specifies the interrupt synchronization mode.</p>


## -syntax

````
typedef enum _INTERRUPT_SYNCHRONIZATION_MODE { 
  InterruptSupportNone            = 0,
  InterruptSynchronizeAll         = 1,
  InterruptSynchronizePerMessage  = 2
} INTERRUPT_SYNCHRONIZATION_MODE;
````


## -enum-fields
<dl>

### -field <a id="InterruptSupportNone"></a><a id="interruptsupportnone"></a><a id="INTERRUPTSUPPORTNONE"></a><b>InterruptSupportNone</b>

<dd>
<p>MSI interrupts are not supported.</p>
</dd>

### -field <a id="InterruptSynchronizeAll"></a><a id="interruptsynchronizeall"></a><a id="INTERRUPTSYNCHRONIZEALL"></a><b>InterruptSynchronizeAll</b>

<dd>
<p>The Storport driver serializes all message signaled interrupts using a single interrupt spin lock. When an interrupt occurs, the Storport driver calls the miniport driver's <a href="storage.hwmsinterruptroutine">HwMSInterruptRoutine</a> routine at DIRQL after acquiring the interrupt spin lock.</p>
</dd>

### -field <a id="InterruptSynchronizePerMessage"></a><a id="interruptsynchronizepermessage"></a><a id="INTERRUPTSYNCHRONIZEPERMESSAGE"></a><b>InterruptSynchronizePerMessage</b>

<dd>
<p>The miniport driver serializes message signaled interrupts on a per message basis. In the synchronization per message mode, the Storport driver calls the miniport driver's <a href="storage.hwmsinterruptroutine">HwMSInterruptRoutine</a> routine at DIRQL   holding the interrupt spin lock of the corresponding  message. For more on the behavior of this synchronization mode, see the remarks section for HwMSInterruptRoutine.</p>
</dd>
</dl>

## -remarks
<p>Miniport drivers define the HBA's interrupt synchronization mode by assigning one of the INTERRUPT_SYNCHRONIZATION_MODE enumeration values to the <b>InterruptSynchronizationMode</b> member of the <a href="..\strmini\ns-strmini--port-configuration-information~r1.md">PORT_CONFIGURATION_INFORMATION</a> structure. </p>

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
<a href="storage.hwmsinterruptroutine">HwMSInterruptRoutine</a>
</dt>
<dt>
<a href="..\strmini\ns-strmini--port-configuration-information~r1.md">PORT_CONFIGURATION_INFORMATION</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportacquiremsispinlock.md">StorPortAcquireMSISpinLock</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportreleasemsispinlock.md">StorPortReleaseMSISpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20INTERRUPT_SYNCHRONIZATION_MODE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
