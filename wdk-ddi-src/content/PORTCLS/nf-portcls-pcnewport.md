---
UID: NF.portcls.PcNewPort
title: PcNewPort
author: windows-driver-content
description: The PcNewPort function creates a new system-supplied port-driver object, whose interface (derived from base class IPort) is specified by a class ID.
old-location: audio\pcnewport.htm
ms.assetid: d948b69c-c5cd-4614-a646-76acb493e8de
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: The PortCls system driver implements the PcNewPort function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcNewPort
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: PcNewPort
req.iface: 
---

# PcNewPort function



## -description
<p>The <b>PcNewPort</b> function creates a new system-supplied port-driver object, whose interface (derived from base class <a href="https://msdn.microsoft.com/library/windows/hardware/ff536842">IPort</a>) is specified by a class ID.</p>


## -syntax

````
NTSTATUS PcNewPort(
  _Out_ PPORT    *OutPort,
  _In_  REFCLSID ClassId
);
````


## -parameters
<dl>

### -param <i>OutPort</i> [out]

<dd>
<p>Output pointer for the port-driver object created by this function. This parameter points to a caller-allocated pointer variable into which the function outputs the pointer to the newly created <a href="https://msdn.microsoft.com/library/windows/hardware/ff536842">IPort</a> object. This object has the port interface that is specified by the <i>ClassId</i> parameter. Specify a valid, non-NULL pointer value for this parameter.</p>
</dd>

### -param <i>ClassId</i> [in]

<dd>
<p>Specifies the type of port interface that is being requested. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p><b>PcNewPort</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>The <i>ClassId</i> parameter can be set to one of the GUIDs in the following table.</p>

<p><b>CLSID_PortDMus</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536879">IPortDMus</a>
</p>

<p><b>CLSID_PortMidi</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536891">IPortMidi</a>
</p>

<p><b>CLSID_PortTopology</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536896">IPortTopology</a>
</p>

<p><b>CLSID_PortWaveCyclic</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536899">IPortWaveCyclic</a>
</p>

<p><b>CLSID_PortWavePci</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536905">IPortWavePci</a>
</p>

<p><b>CLSID_PortWaveRT</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536920">IPortWaveRT</a>
</p>

<p> </p>

<p><b>CLSID_PortDMus</b> is defined in header file dmusicks.h. The other four GUIDs in the preceding table are defined in portcls.h.</p>

<p>In Microsoft Windows XP and later, the MIDI and DirectMusic port drivers share the same internal software implementation. This means that the <b>CLSID_PortMidi</b> GUID is equivalent to <b>CLSID_PortDMus</b>.</p>

<p>For more information about creating port and miniport drivers for subdevices, see <a href="NULL">Subdevice Creation</a>.</p>

<p>The <i>OutPort</i> parameter follows the <a href="NULL">reference-counting conventions for COM objects</a>. </p>

<p>The <i>ClassId</i> parameter can be set to one of the GUIDs in the following table.</p>

<p><b>CLSID_PortDMus</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536879">IPortDMus</a>
</p>

<p><b>CLSID_PortMidi</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536891">IPortMidi</a>
</p>

<p><b>CLSID_PortTopology</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536896">IPortTopology</a>
</p>

<p><b>CLSID_PortWaveCyclic</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536899">IPortWaveCyclic</a>
</p>

<p><b>CLSID_PortWavePci</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536905">IPortWavePci</a>
</p>

<p><b>CLSID_PortWaveRT</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536920">IPortWaveRT</a>
</p>

<p> </p>

<p><b>CLSID_PortDMus</b> is defined in header file dmusicks.h. The other four GUIDs in the preceding table are defined in portcls.h.</p>

<p>In Microsoft Windows XP and later, the MIDI and DirectMusic port drivers share the same internal software implementation. This means that the <b>CLSID_PortMidi</b> GUID is equivalent to <b>CLSID_PortDMus</b>.</p>

<p>For more information about creating port and miniport drivers for subdevices, see <a href="NULL">Subdevice Creation</a>.</p>

<p>The <i>OutPort</i> parameter follows the <a href="NULL">reference-counting conventions for COM objects</a>. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>The PortCls system driver implements the PcNewPort function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.</p>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536842">IPort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536879">IPortDMus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536891">IPortMidi</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536896">IPortTopology</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536899">IPortWaveCyclic</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536905">IPortWavePci</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536920">IPortWaveRT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcNewPort function%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
