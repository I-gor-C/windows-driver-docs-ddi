---
UID: NF.portcls.IPortWavePci.Notify
title: IPortWavePci::Notify
author: windows-driver-content
description: The Notify method notifies the port driver that an interrupt indicating the progress of the DMA pointer has occurred.
old-location: audio\iportwavepci_notify.htm
old-project: audio
ms.assetid: fa65b3c3-196c-4cf4-8c9e-c0c9a33b2881
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IPortWavePci, Notify, IPortWavePci::Notify
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortWavePci.Notify
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: IPortWavePci
---

# IPortWavePci::Notify method



## -description
<p>The <code>Notify</code> method notifies the port driver that an interrupt indicating the progress of the DMA pointer has occurred.</p>


## -syntax

````
void Notify(
  [in] PSERVICEGROUP ServiceGroup
);
````


## -parameters
<dl>

### -param <i>ServiceGroup</i> [in]

<dd>
<p>A pointer to the miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536994">IServiceGroup</a> object.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Some miniport drivers call this method from an ISR in response to a hardware interrupt after having cleared the interrupt source. Other drivers call this method from a timer DPC that is scheduled to run at regular intervals. As a general rule, only drivers that manage a single render stream from KMixer should rely on hardware interrupts. Drivers that support DirectSound hardware acceleration should turn off hardware interrupts and use timer DPCs instead. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536909">IPortWavePciStream::GetMapping</a>.</p>

<p>Although the miniport driver is free to choose its own technique for determining when to call this method, this method should be called frequently enough to allow the port driver to fire pending position and clock events at regular intervals. Timing for this method is not as critical as it is for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536903">IPortWaveCyclic::Notify</a> method, however.</p>

<p>When an adapter driver installs an ISR, it submits a <i>ServiceContext</i> parameter along with the ISR's entry point (for details, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559930">Providing ISR Context Information</a>). When the interrupt occurs, the operating system calls the ISR and passes <i>ServiceContext</i> as a call parameter to the ISR. Although the meaning of the <i>ServiceContext</i> parameter is known only to the driver developer, it is typically a pointer to the miniport object. The ISR uses this pointer to access information about the miniport object.</p>

<p>The <i>ServiceGroup</i> parameter follows the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

<p>Some miniport drivers call this method from an ISR in response to a hardware interrupt after having cleared the interrupt source. Other drivers call this method from a timer DPC that is scheduled to run at regular intervals. As a general rule, only drivers that manage a single render stream from KMixer should rely on hardware interrupts. Drivers that support DirectSound hardware acceleration should turn off hardware interrupts and use timer DPCs instead. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536909">IPortWavePciStream::GetMapping</a>.</p>

<p>Although the miniport driver is free to choose its own technique for determining when to call this method, this method should be called frequently enough to allow the port driver to fire pending position and clock events at regular intervals. Timing for this method is not as critical as it is for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536903">IPortWaveCyclic::Notify</a> method, however.</p>

<p>When an adapter driver installs an ISR, it submits a <i>ServiceContext</i> parameter along with the ISR's entry point (for details, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559930">Providing ISR Context Information</a>). When the interrupt occurs, the operating system calls the ISR and passes <i>ServiceContext</i> as a call parameter to the ISR. Although the meaning of the <i>ServiceContext</i> parameter is known only to the driver developer, it is typically a pointer to the miniport object. The ISR uses this pointer to access information about the miniport object.</p>

<p>The <i>ServiceGroup</i> parameter follows the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536905">IPortWavePci</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536994">IServiceGroup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536909">IPortWavePciStream::GetMapping</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536903">IPortWaveCyclic::Notify</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortWavePci::Notify method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
