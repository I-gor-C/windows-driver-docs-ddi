---
UID: NS.wdfinterrupt._WDF_INTERRUPT_INFO
title: WDF_INTERRUPT_INFO
author: windows-driver-content
description: The WDF_INTERRUPT_INFO structure contains information about a device's interrupt resource.
old-location: wdf\wdf_interrupt_info.htm
old-project: wdf
ms.assetid: 7e626306-6ad9-4d99-a578-60bf69a3e73d
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_INTERRUPT_INFO, WDF_INTERRUPT_INFO, *PWDF_INTERRUPT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_INTERRUPT_INFO
req.alt-loc: wdfinterrupt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DIRQL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_INTERRUPT_INFO structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_INTERRUPT_INFO</b> structure contains information about a device's interrupt resource.</p>


## -syntax

````
typedef struct _WDF_INTERRUPT_INFO {
  ULONG                  Size;
  ULONG64                Reserved1;
  KAFFINITY              TargetProcessorSet;
  ULONG                  Reserved2;
  ULONG                  MessageNumber;
  ULONG                  Vector;
  KIRQL                  Irql;
  KINTERRUPT_MODE        Mode;
  WDF_INTERRUPT_POLARITY Polarity;
  BOOLEAN                MessageSignaled;
  UCHAR                  ShareDisposition;
  USHORT                 Group;
} WDF_INTERRUPT_INFO, *PWDF_INTERRUPT_INFO;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field Reserved1

<dd>
<p>This member is reserved for future use. </p>
</dd>

### -field TargetProcessorSet

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a>-typed value that specifies the interrupt's processor affinity.</p>
</dd>

### -field Reserved2

<dd>
<p>This member is reserved for future use. </p>
</dd>

### -field MessageNumber

<dd>
<p>If the <b>MessageSignaled</b> member is <b>TRUE</b>, this is the interrupt's message number.</p>
</dd>

### -field Vector

<dd>
<p>The interrupt vector.</p>
</dd>

### -field Irql

<dd>
<p>The IRQL at which the device interrupts.</p>
</dd>

### -field Mode

<dd>
<p>A <a href="..\wdm\ne-wdm--kinterrupt-mode.md">KINTERRUPT_MODE</a>-typed enumerator that indicates whether the interrupt is level-triggered or edge-triggered.</p>
</dd>

### -field Polarity

<dd>
<p>A <a href="..\wudfinterrupt\ne-wudfinterrupt--wdf-interrupt-polarity.md">WDF_INTERRUPT_POLARITY</a>-typed enumerator that identifies the interrupt signal's polarity.</p>
</dd>

### -field MessageSignaled

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the interrupt is message-signaled. If <b>FALSE</b>, the interrupt is not message-signaled.</p>
</dd>

### -field ShareDisposition

<dd>
<p>A CM_SHARE_DISPOSITION-typed enumerator that indicates whether the interrupt is being shared. The value is <b>CmResourceShareShared</b> if the interrupt is being shared or <b>CmResourceShareDeviceExclusive</b> if the interrupt is not being shared. The CM_SHARE_DISPOSITION enumeration type is defined in <i>Wdm.h</i>.</p>
</dd>

### -field Group

<dd>
<p>A value that identifies the processor group that the <b>TargetProcessorSet</b> member applies to. This value is zero if the computer has only one processor group or if the operating system does not support processor groups. The <b>Group</b> member is available in version 1.9 and later versions of KMDF.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_INTERRUPT_INFO</b> structure is used as input to the <a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptgetinfo.md">WdfInterruptGetInfo</a> method. To initialize a <b>WDF_INTERRUPT_INFO</b> structure, your driver should call <a href="..\wudfinterrupt\nf-wudfinterrupt-wdf-interrupt-info-init.md">WDF_INTERRUPT_INFO_INIT</a> before calling <b>WdfInterruptGetInfo</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfinterrupt.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptgetinfo.md">WdfInterruptGetInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--kinterrupt-mode.md">KINTERRUPT_MODE</a>
</dt>
<dt>
<a href="..\wudfinterrupt\nf-wudfinterrupt-wdf-interrupt-info-init.md">WDF_INTERRUPT_INFO_INIT</a>
</dt>
<dt>
<a href="..\wudfinterrupt\ne-wudfinterrupt--wdf-interrupt-polarity.md">WDF_INTERRUPT_POLARITY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_INTERRUPT_INFO structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
