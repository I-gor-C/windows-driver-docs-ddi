---
UID: NF.portcls.PcNewMiniport
title: PcNewMiniport
author: windows-driver-content
description: The PcNewMiniport function creates an instance of one of the system-supplied miniport drivers that are built into the PortCls system driver, portcls.sys.
old-location: audio\pcnewminiport.htm
ms.assetid: 15046dc7-42ae-4ebe-acb9-2b0bbad1e833
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: The PortCls system driver implements the PcNewMiniport function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcNewMiniport
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
ms.keywords: PcNewMiniport
req.iface: 
---

# PcNewMiniport function



## -description
<p>The <b>PcNewMiniport</b> function creates an instance of one of the system-supplied miniport drivers that are built into the PortCls system driver, portcls.sys. A class ID specifies which of these miniport drivers to instantiate. The driver supports a miniport interface that is derived from <a href="https://msdn.microsoft.com/library/windows/hardware/ff536698">IMiniport</a>.</p>


## -syntax

````
NTSTATUS PcNewMiniport(
  _Out_ PMINIPORT *OutMiniport,
  _In_  REFCLSID  ClassId
);
````


## -parameters
<dl>

### -param <i>OutMiniport</i> [out]

<dd>
<p>Output pointer for the miniport-driver object created by this function. This parameter points to a caller-allocated pointer variable into which the function outputs a reference to the newly created <a href="https://msdn.microsoft.com/library/windows/hardware/ff536698">IMiniport</a> object. This object is an instance of the miniport driver that is specified by the <i>ClassId</i> parameter. Specify a valid, non-NULL pointer value for this parameter.</p>
</dd>

### -param <i>ClassId</i> [in]

<dd>
<p>Specifies the miniport interface that is being requested. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p><b>PcNewMiniport</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>The system-supplied miniport drivers for MPU-401 UARTs and OPL3 synthesizers can be instantiated by calling <b>PcNewMiniport</b> These are built-in miniport drivers that are provided with the portcls.sys system driver. Miniport drivers that are part of a vendor's adapter driver are not created in this way.</p>

<p>The <i>ClassId</i> parameter can be set to one of the GUIDs in the following table.</p>

<p><b>CLSID_MiniportDriverDMusUART</b></p>

<p>DMusUART miniport driver for MPU-401 synth device. Exposes <a href="https://msdn.microsoft.com/library/windows/hardware/ff536699">IMiniportDMus</a> interface for use with <a href="https://msdn.microsoft.com/library/windows/hardware/ff536879">IPortDMus</a> port object.</p>

<p><b>CLSID_MiniportDriverDMusUARTCapture</b></p>

<p>DMusUARTCapture miniport driver for MPU-401 capture device. Exposes <a href="https://msdn.microsoft.com/library/windows/hardware/ff536699">IMiniportDMus</a> interface for use with <a href="https://msdn.microsoft.com/library/windows/hardware/ff536879">IPortDMus</a> port object.</p>

<p><b>CLSID_MiniportDriverFmSynth</b></p>

<p>FmSynth miniport driver for FM synth device. Exposes <a href="https://msdn.microsoft.com/library/windows/hardware/ff536703">IMiniportMidi</a> interface for use with <a href="https://msdn.microsoft.com/library/windows/hardware/ff536891">IPortMidi</a> port object.</p>

<p><b>CLSID_MiniportDriverFmSynthWithVol</b></p>

<p>Same as the preceding entry, except that the driver also supports a volume node.</p>

<p><b>CLSID_MiniportDriverUart</b></p>

<p>UART miniport driver for MPU-401 synth device. Exposes <a href="https://msdn.microsoft.com/library/windows/hardware/ff536703">IMiniportMidi</a> interface for use with <a href="https://msdn.microsoft.com/library/windows/hardware/ff536891">IPortMidi</a> port object. Obsolete.</p>

<p> </p>

<p>The first two GUIDs in the preceding table are defined in header file dmusicks.h; the last three are defined in portcls.h.</p>

<p>The DMusUART miniport driver outputs MIDI data to a synth device with a pure MPU-401 MIDI interface. To produce sound, this device needs an external MIDI sound module attached to it.</p>

<p>The DMusUARTCapture miniport driver inputs MIDI data from a capture device with a pure MPU-401 interface.</p>

<p>The FMSynth miniport driver outputs MIDI data to a synth device that implements OPL3-style FM synthesis. The <b>CLSID_MiniportDriverFmSynth</b> GUID is appropriate for most FM synth devices. However, devices such as the Windows Sound System that do not provide a hardware volume control after the FM synth should use the <b>CLSID_MiniportDriverFmSynthWithVol</b> GUID instead. In Windows Server SP1 and later, the FMSynth miniport driver is available only in 32-bit versions of the operating system.</p>

<p>The UART miniport driver is obsolete. New adapter driver code should use the DMusUART miniport driver, which supersedes UART and implements a superset of its functionality.</p>

<p>Microsoft provides the source code for the DMusUART and FMSynth miniport drivers, which can serve as a starting point for hardware vendors who might need to extend these drivers to manage additional device capabilities. Look in the sample audio drivers in the Windows Driver Kit (WDK).</p>

<p>See <a href="NULL">Subdevice Creation</a> For more information about creating port and miniport drivers for subdevices.</p>

<p>The <i>OutMiniport</i> parameter follows the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

<p>The system-supplied miniport drivers for MPU-401 UARTs and OPL3 synthesizers can be instantiated by calling <b>PcNewMiniport</b> These are built-in miniport drivers that are provided with the portcls.sys system driver. Miniport drivers that are part of a vendor's adapter driver are not created in this way.</p>

<p>The <i>ClassId</i> parameter can be set to one of the GUIDs in the following table.</p>

<p><b>CLSID_MiniportDriverDMusUART</b></p>

<p>DMusUART miniport driver for MPU-401 synth device. Exposes <a href="https://msdn.microsoft.com/library/windows/hardware/ff536699">IMiniportDMus</a> interface for use with <a href="https://msdn.microsoft.com/library/windows/hardware/ff536879">IPortDMus</a> port object.</p>

<p><b>CLSID_MiniportDriverDMusUARTCapture</b></p>

<p>DMusUARTCapture miniport driver for MPU-401 capture device. Exposes <a href="https://msdn.microsoft.com/library/windows/hardware/ff536699">IMiniportDMus</a> interface for use with <a href="https://msdn.microsoft.com/library/windows/hardware/ff536879">IPortDMus</a> port object.</p>

<p><b>CLSID_MiniportDriverFmSynth</b></p>

<p>FmSynth miniport driver for FM synth device. Exposes <a href="https://msdn.microsoft.com/library/windows/hardware/ff536703">IMiniportMidi</a> interface for use with <a href="https://msdn.microsoft.com/library/windows/hardware/ff536891">IPortMidi</a> port object.</p>

<p><b>CLSID_MiniportDriverFmSynthWithVol</b></p>

<p>Same as the preceding entry, except that the driver also supports a volume node.</p>

<p><b>CLSID_MiniportDriverUart</b></p>

<p>UART miniport driver for MPU-401 synth device. Exposes <a href="https://msdn.microsoft.com/library/windows/hardware/ff536703">IMiniportMidi</a> interface for use with <a href="https://msdn.microsoft.com/library/windows/hardware/ff536891">IPortMidi</a> port object. Obsolete.</p>

<p> </p>

<p>The first two GUIDs in the preceding table are defined in header file dmusicks.h; the last three are defined in portcls.h.</p>

<p>The DMusUART miniport driver outputs MIDI data to a synth device with a pure MPU-401 MIDI interface. To produce sound, this device needs an external MIDI sound module attached to it.</p>

<p>The DMusUARTCapture miniport driver inputs MIDI data from a capture device with a pure MPU-401 interface.</p>

<p>The FMSynth miniport driver outputs MIDI data to a synth device that implements OPL3-style FM synthesis. The <b>CLSID_MiniportDriverFmSynth</b> GUID is appropriate for most FM synth devices. However, devices such as the Windows Sound System that do not provide a hardware volume control after the FM synth should use the <b>CLSID_MiniportDriverFmSynthWithVol</b> GUID instead. In Windows Server SP1 and later, the FMSynth miniport driver is available only in 32-bit versions of the operating system.</p>

<p>The UART miniport driver is obsolete. New adapter driver code should use the DMusUART miniport driver, which supersedes UART and implements a superset of its functionality.</p>

<p>Microsoft provides the source code for the DMusUART and FMSynth miniport drivers, which can serve as a starting point for hardware vendors who might need to extend these drivers to manage additional device capabilities. Look in the sample audio drivers in the Windows Driver Kit (WDK).</p>

<p>See <a href="NULL">Subdevice Creation</a> For more information about creating port and miniport drivers for subdevices.</p>

<p>The <i>OutMiniport</i> parameter follows the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

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
<p>The PortCls system driver implements the PcNewMiniport function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536698">IMiniport</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536699">IMiniportDMus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536703">IMiniportMidi</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536879">IPortDMus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536891">IPortMidi</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcNewMiniport function%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
