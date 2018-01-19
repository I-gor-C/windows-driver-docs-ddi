---
UID : NI:usbscan.IOCTL_WRITE_REGISTERS
title : IOCTL_WRITE_REGISTERS
author : windows-driver-content
description : Writes to USB device registers, using the control pipe.
old-location : image\ioctl_write_registers.htm
old-project : image
ms.assetid : c7175b39-9db2-4903-bb50-bb0c97fda471
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : _RAW_PIPE_TYPE, RAW_PIPE_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : usbscan.h
req.include-header : Usbscan.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_WRITE_REGISTERS
req.alt-loc : Usbscan.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : RAW_PIPE_TYPE
req.product : Windows 10 or later.
---

# IOCTL_WRITE_REGISTERS IOCTL
Writes to USB device registers, using the control pipe.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
Pointer to an <a href="..\usbscan\ns-usbscan-_io_block.md">IO_BLOCK</a> structure.

### Input Buffer Length
Size of the input buffer.

### Output Buffer
<b>NULL</b>

### Output Buffer Length
Zero.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.

    ## Remarks
        Device handle, obtained by calling <a href="https://msdn.microsoft.com/80a96083-4de9-4422-9705-b8ad2b6cbd1b">CreateFile</a>.

IOCTL_WRITE_REGISTERS

Pointer to an <a href="..\usbscan\ns-usbscan-_io_block.md">IO_BLOCK</a> structure.

Size of the input buffer.

<b>NULL</b>.

Zero.

Pointer to a location to receive the number of bytes written.

Optional pointer to an OVERLAPPED structure (described in the Microsoft Windows SDK documentation).

When the <b>DeviceloControl</b> function is called with the IOCTL_WRITE_REGISTERS I/O control code, the caller must specify the address of an <a href="..\usbscan\ns-usbscan-_io_block.md">IO_BLOCK</a> structure as the function's <i>lpInBuffer</i> parameter.

Using the IO_BLOCK contents, the kernel-mode driver creates a <a href="..\usb\ns-usb-_urb.md">URB</a> that contains a <a href="..\usb\ns-usb-_urb_control_vendor_or_class_request.md">_URB_CONTROL_VENDOR_OR_CLASS_REQUEST</a> structure.

The following table indicates the values assigned to _URB_CONTROL_VENDOR_OR_CLASS_REQUEST structure members.

<b>TransferFlags</b>

0

<b>TransferBufferLength</b>

<i>pIoBlock</i>-&gt;<b>uLength</b>

<b>TransferBuffer</b>

<i>pIoBlock</i>-&gt;<b>pbyData</b>

<b>TransferBufferMDL</b>

<b>NULL</b>

<b>RequestTypeReservedBits</b>

0x40

<b>Request</b>

(<i>pIoBlock</i>-&gt;<b>uLength</b> &gt; 1) ? 0x04 : 0x0C

<b>Value</b>

(SHORT)<i>pIoBlock</i>-&gt;<b>uOffset</b>

<b>Index</b>

<i>pIoBlock</i>-&gt;<b>uIndex</b>

For more information, see <a href="https://msdn.microsoft.com/f9216d3c-4930-4c26-8eac-6ee500b038e0">Accessing Kernel-Mode Drivers for Still Image Devices</a>.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | usbscan.h (include Usbscan.h) |
| **IRQL** |  |