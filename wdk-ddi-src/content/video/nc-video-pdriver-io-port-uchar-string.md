---
UID: NC.video.PDRIVER_IO_PORT_UCHAR_STRING
title: PDRIVER_IO_PORT_UCHAR_STRING
author: windows-driver-content
description: SvgaHwIoPortUcharString traps an I/O port to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of UCHAR-sized data.
old-location: display\svgahwioportucharstring.htm
old-project: display
ms.assetid: 7158cd6c-a662-46e8-bb7c-ea852797c39e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VHF_CONFIG, VHF_CONFIG, *PVHF_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SvgaHwIoPortUcharString
req.alt-loc: video.h
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

# PDRIVER_IO_PORT_UCHAR_STRING callback



## -description
<p><i>SvgaHwIoPortUcharString</i> traps an I/O port to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of UCHAR-sized data.</p>


## -prototype

````
PDRIVER_IO_PORT_UCHAR_STRING SvgaHwIoPortUcharString;

VP_STATUS SvgaHwIoPortUcharString(
   ULONG_PTR Context,
   ULONG     Port,
   UCHAR     AccessMode,
   PUCHAR    Data,
   ULONG     DataLength
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> 

<dd>
<p>Specifies the miniport driver-determined context value that was set in the <b>EmulatorAccessEntriesContext</b> member of VIDEO_PORT_CONFIG_INFO.</p>
</dd>

### -param <i>Port</i> 

<dd>
<p>Specifies the mapped I/O port.</p>
</dd>

### -param <i>AccessMode</i> 

<dd>
<p>Specifies the type of access allowed, which can be one or a combination (ORed) of the following values:</p>
<p>
<dl>

### -param EMULATOR_READ_ACCESS


### -param EMULATOR_WRITE_ACCESS

</dl>
</p>
</dd>

### -param <i>Data</i> 

<dd>
<p>Pointer to the UCHAR string to be transferred. One character at a time is hooked out until the whole string is transferred.</p>
</dd>

### -param <i>DataLength</i> 

<dd>
<p>Specifies the number of UCHAR values in the string.</p>
</dd>
</dl>

## -returns
<p><i>SvgaHwIoPortUcharString</i> returns the final status of the operation.</p>

## -remarks
<p>Only miniport drivers of VGA-compatible SVGA adapters have <i>SvgaHwIoPortXxx</i> functions. (See <a href="https://msdn.microsoft.com/library/windows/hardware/ff569908">SVGA Functions</a>.)</p>

<p><i>SvgaHwIoPortUcharString</i> intercepts any byte access attempted by a full-screen MS-DOS application issuing either or both of the instructions <b>REP OUTSB DX, ESI</b> and <b>REP INSB EDI, DX</b>.</p>

<p>If the miniport driver enables the <i>Port</i> for direct access by calling <b>VideoSetTrappedEmulatorPorts</b>, its <i>SvgaHwIoPortUcharString</i> function will not be called. Such an application then will have direct access to the I/O port, unless the miniport driver disables the port with another call to <b>VideoSetTrappedEmulatorPorts</b>.</p>

<p>If one or more application-issued x86 <b>INSB</b> or <b>OUTSB</b> instructions might affect the state of the VGA-compatible adapter sequencer register, miscellaneous output register, or any adapter-specific register and, thereby, cause the machine to hang, the miniport driver must <i>not</i> enable the port for direct access by calling <b>VideoPortSetTrappedEmulatorPorts</b>.</p>

<p><i>SvgaHwIoPortUcharString</i> must buffer subsequent instructions from the application and check that none can hang the machine. If the application issues any sequence of instructions that might hang the machine, <i>SvgaHwIoPortUcharString</i> must discard the buffered instructions. Otherwise, it should output them, a UCHAR at a time, to the specified, mapped I/O port.</p>

<p><i>SvgaHwIoPortUcharString</i> should be made pageable.</p>

<p>Only miniport drivers of VGA-compatible SVGA adapters have <i>SvgaHwIoPortXxx</i> functions. (See <a href="https://msdn.microsoft.com/library/windows/hardware/ff569908">SVGA Functions</a>.)</p>

<p><i>SvgaHwIoPortUcharString</i> intercepts any byte access attempted by a full-screen MS-DOS application issuing either or both of the instructions <b>REP OUTSB DX, ESI</b> and <b>REP INSB EDI, DX</b>.</p>

<p>If the miniport driver enables the <i>Port</i> for direct access by calling <b>VideoSetTrappedEmulatorPorts</b>, its <i>SvgaHwIoPortUcharString</i> function will not be called. Such an application then will have direct access to the I/O port, unless the miniport driver disables the port with another call to <b>VideoSetTrappedEmulatorPorts</b>.</p>

<p>If one or more application-issued x86 <b>INSB</b> or <b>OUTSB</b> instructions might affect the state of the VGA-compatible adapter sequencer register, miscellaneous output register, or any adapter-specific register and, thereby, cause the machine to hang, the miniport driver must <i>not</i> enable the port for direct access by calling <b>VideoPortSetTrappedEmulatorPorts</b>.</p>

<p><i>SvgaHwIoPortUcharString</i> must buffer subsequent instructions from the application and check that none can hang the machine. If the application issues any sequence of instructions that might hang the machine, <i>SvgaHwIoPortUcharString</i> must discard the buffered instructions. Otherwise, it should output them, a UCHAR at a time, to the specified, mapped I/O port.</p>

<p><i>SvgaHwIoPortUcharString</i> should be made pageable.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564131">EMULATOR_ACCESS_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569908">SVGA Functions</a>
</dt>
<dt>
<a href="..\video\nc-video-pdriver-io-port-uchar.md">SvgaHwIoPortUchar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570498">VIDEO_ACCESS_RANGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570531">VIDEO_PORT_CONFIG_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570310">VideoPortGetDeviceBase</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570366">VideoPortSetTrappedEmulatorPorts</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PDRIVER_IO_PORT_UCHAR_STRING callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
