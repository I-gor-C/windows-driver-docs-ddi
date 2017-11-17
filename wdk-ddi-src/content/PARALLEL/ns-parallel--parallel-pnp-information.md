---
UID: NS.parallel._PARALLEL_PNP_INFORMATION
title: PARALLEL_PNP_INFORMATION
author: windows-driver-content
description: The PARALLEL_PNP_INFORMATION structure specifies information about the capabilities of a parallel port.
old-location: parports\parallel_pnp_information.htm
ms.assetid: 9288fc11-e19b-46dd-95e4-6de8c7cdc61d
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: parports
req.header: parallel.h
req.include-header: Parallel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PARALLEL_PNP_INFORMATION
req.alt-loc: parallel.h
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
ms.keywords: PARALLEL_PNP_INFORMATION, PARALLEL_PNP_INFORMATION, *PPARALLEL_PNP_INFORMATION
req.iface: 
---

# PARALLEL_PNP_INFORMATION structure



## -description
<p>The PARALLEL_PNP_INFORMATION structure specifies information about the capabilities of a parallel port.</p>


## -syntax

````
typedef struct _PARALLEL_PNP_INFORMATION {
  PHYSICAL_ADDRESS             OriginalEcpController;
  PUCHAR                       EcpController;
  ULONG                        SpanOfEcpController;
  ULONG                        PortNumber;
  ULONG                        HardwareCapabilities;
  PPARALLEL_SET_CHIP_MODE      TrySetChipMode;
  PPARALLEL_CLEAR_CHIP_MODE    ClearChipMode;
  ULONG                        FifoDepth;
  ULONG                        FifoWidth;
  PHYSICAL_ADDRESS             EppControllerPhysicalAddress;
  ULONG                        SpanOfEppController;
  ULONG                        Ieee1284_3DeviceCount;
  PPARALLEL_TRY_SELECT_ROUTINE TrySelectDevice;
  PPARALLEL_DESELECT_ROUTINE   DeselectDevice;
  PVOID                        Context;
  ULONG                        CurrentMode;
  PWSTR                        PortName;
} PARALLEL_PNP_INFORMATION, *PPARALLEL_PNP_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>OriginalEcpController</b>

<dd>
<p>Specifies the base physical address that the system-supplied function driver for parallel ports uses to control the ECP operation of the parallel port.</p>
</dd>

### -field <b>EcpController</b>

<dd>
<p>Pointer to the I/O port resource that is used to control the port in ECP mode.</p>
</dd>

### -field <b>SpanOfEcpController</b>

<dd>
<p>Specifies the size, in bytes, of the I/O port resource.</p>
</dd>

### -field <b>PortNumber</b>

<dd>
<p>Not used.</p>
</dd>

### -field <b>HardwareCapabilities</b>

<dd>
<p>Specifies the hardware capabilities of the parallel port. The following capabilities can be set using a bitwise OR of the following constants:</p>
<p></p>
<dl>

### -field <a id="PPT_1284_3_PRESENT"></a><a id="ppt_1284_3_present"></a>PPT_1284_3_PRESENT

<dd></dd>

### -field <a id="PPT_BYTE_PRESENT_"></a><a id="ppt_byte_present_"></a>PPT_BYTE_PRESENT 

<dd></dd>

### -field <a id="PPT_ECP_PRESENT_"></a><a id="ppt_ecp_present_"></a>PPT_ECP_PRESENT 

<dd></dd>

### -field <a id="PPT_EPP_32_PRESENT_"></a><a id="ppt_epp_32_present_"></a>PPT_EPP_32_PRESENT 

<dd></dd>

### -field <a id="PPT_EPP_PRESENT_"></a><a id="ppt_epp_present_"></a>PPT_EPP_PRESENT 

<dd></dd>

### -field <a id="PT_NO_HARDWARE_PRESENT_"></a><a id="pt_no_hardware_present_"></a>PT_NO_HARDWARE_PRESENT 

<dd></dd>
</dl>
</dd>

### -field <b>TrySetChipMode</b>

<dd>
<p>Pointer to the system-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff544542">PPARALLEL_SET_CHIP_MODE</a> callback that a kernel-mode driver can use to change the operating mode of the parallel port.</p>
</dd>

### -field <b>ClearChipMode</b>

<dd>
<p>Pointer to the system-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff544398">PPARALLEL_CLEAR_CHIP_MODE</a> callback that a kernel-mode driver can use to clear the operating mode of the parallel port.</p>
</dd>

### -field <b>FifoDepth</b>

<dd>
<p>Specifies the size, in words, of the hardware first in/first out (FIFO) buffer. The FIFO word size, in bits, is the value of <b>FifoWidth</b>.</p>
</dd>

### -field <b>FifoWidth</b>

<dd>
<p>Specifies the FIFO word size, in bits, which is the number of bits handled in parallel.</p>
</dd>

### -field <b>EppControllerPhysicalAddress</b>

<dd>
<p>Not used.</p>
</dd>

### -field <b>SpanOfEppController</b>

<dd>
<p>Not used.</p>
</dd>

### -field <b>Ieee1284_3DeviceCount</b>

<dd>
<p>Specifies the number of daisy-chain devices currently attached to a parallel port. In Microsoft Windows XP, from zero to two devices can be simultaneously connected to a parallel port. In Windows 2000, from zero to four devices can be simultaneously connected to a parallel port.</p>
</dd>

### -field <b>TrySelectDevice</b>

<dd>
<p>Pointer to the system-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff544767">PPARALLEL_TRY_SELECT_ROUTINE</a> callback that a kernel-mode driver can use to attempt to select an IEEE 1284.3 device.</p>
</dd>

### -field <b>DeselectDevice</b>

<dd>
<p>Pointer to the system-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff544504">PPARALLEL_DESELECT_ROUTINE</a> callback that a kernel-mode driver can use to deselect an IEEE 1284.3 device.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>Pointer to the device extension of a parallel port's functional device object (<a href="wdkgloss.f#wdkgloss.fdo#wdkgloss.fdo"><i>FDO</i></a>).</p>
</dd>

### -field <b>CurrentMode</b>

<dd>
<p>The current operating mode of the parallel port.</p>
</dd>

### -field <b>PortName</b>

<dd>
<p>The symbolic link name of the parallel port.</p>
</dd>
</dl>

## -remarks
<p>For more information, see <a href="https://msdn.microsoft.com/d8ae2296-05b6-419a-93cc-00fcb12d41fe">Obtaining Information About a ParallelPort</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Parallel.h (include Parallel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543996">IOCTL_INTERNAL_GET_MORE_PARALLEL_PORT_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543997">IOCTL_INTERNAL_GET_PARALLEL_PNP_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544002">IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544207">MORE_PARALLEL_PORT_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544322">PARALLEL_PORT_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544398">PPARALLEL_CLEAR_CHIP_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544504">PPARALLEL_DESELECT_ROUTINE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544542">PPARALLEL_SET_CHIP_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544767">PPARALLEL_TRY_SELECT_ROUTINE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PARALLEL_PNP_INFORMATION structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
