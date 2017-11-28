---
UID: NI.acpiioct.IOCTL_ACPI_EVAL_METHOD
title: IOCTL_ACPI_EVAL_METHOD
author: windows-driver-content
description: A driver for a device can use the IOCTL_ACPI_EVAL_METHOD device control request to synchronously evaluate an ACPI control method that is supported by the device.
old-location: acpi\ioctl_acpi_eval_method.htm
old-project: acpi
ms.assetid: 3f7f904c-1d5e-4647-a566-1ec447a4cd13
ms.author: windowsdriverdev
ms.date: 11/16/2017
ms.keywords: UNIT_ISOCH_PARAMS, UNIT_ISOCH_PARAMS, *PUNIT_ISOCH_PARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: acpiioct.h
req.include-header: Acpiioct.h
req.target-type: Windows
req.target-min-winverclnt: Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_ACPI_EVAL_METHOD
req.alt-loc: Acpiioct.h
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
---

# IOCTL_ACPI_EVAL_METHOD IOCTL



## -description
<p>A driver for a device can use the IOCTL_ACPI_EVAL_METHOD device control request to synchronously evaluate an ACPI control method that is supported by the device. The driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548318">IoBuildDeviceIoControlRequest</a> and pass the following input and output parameters to build this request.</p>


## -ioctlparameters

### -input-buffer
<p>Set the <b>IoBuildDeviceIoControlRequest</b> input parameters as follows:</p>

<p><i>IoControlCode</i> is set to IOCTL_ACPI_EVAL_METHOD.</p>

<p><i>DeviceObject</i> is set to a pointer to the physical device object (PDO) of the device.</p>

<p><i>InputBuffer</i> is set to a pointer to an input buffer structure that depends on the type of input arguments to be passed to the control method. For more information about the type of input arguments that this IOCTL supports, see the Remarks section later in this topic.</p>

<p><i>InputBufferLength</i> is set to the size, in bytes, of the input buffer that is supplied by <i>InputBuffer</i>.</p>

<p><i>OutputBufferLength</i> supplies the size, in bytes, of the output buffer that is supplied by <i>OutputBuffer</i>.</p>

<p><i>InternalDeviceIoControl</i> is set to <b>FALSE</b>.</p>

<p><i>Event</i> is set to a pointer to a caller-allocated and initialized event object.</p>

### -input-buffer-length
<p><i>InputBufferLength</i> is set to the size, in bytes, of the input buffer that is supplied by <i>InputBuffer</i>.</p>

<p><i>InputBufferLength</i> is set to the size, in bytes, of the input buffer that is supplied by <i>InputBuffer</i>.</p>

### -output-buffer
<p>Set the <b>IoBuildDeviceIoControlRequest</b> output parameters as follows:</p>

<p><i>OutputBuffer</i> supplies a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536123">ACPI_EVAL_OUTPUT_BUFFER</a> structure that contains the output arguments from the control method.</p>

<p><i>IoStatusBlock</i> is set to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure.</p>

<p>Set the <b>IoBuildDeviceIoControlRequest</b> output parameters as follows:</p>

<p><i>OutputBuffer</i> supplies a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536123">ACPI_EVAL_OUTPUT_BUFFER</a> structure that contains the output arguments from the control method.</p>

<p><i>IoStatusBlock</i> is set to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure.</p>

<p>Set the <b>IoBuildDeviceIoControlRequest</b> output parameters as follows:</p>

<p><i>OutputBuffer</i> supplies a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536123">ACPI_EVAL_OUTPUT_BUFFER</a> structure that contains the output arguments from the control method.</p>

<p><i>IoStatusBlock</i> is set to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure.</p>

### -output-buffer-length
<p><i>OutputBufferLength</i> supplies the size, in bytes, of the output buffer that is supplied by <i>OutputBuffer</i>.</p>

<p><i>OutputBufferLength</i> supplies the size, in bytes, of the output buffer that is supplied by <i>OutputBuffer</i>.</p>

<p><i>OutputBufferLength</i> supplies the size, in bytes, of the output buffer that is supplied by <i>OutputBuffer</i>.</p>

<p><i>OutputBufferLength</i> supplies the size, in bytes, of the output buffer that is supplied by <i>OutputBuffer</i>.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>If the request succeeds, <i>IoStatusBlock</i>-&gt;<b>Status</b> is set to STATUS_SUCCESS; otherwise, the <b>Status</b> member is set to an error code. If the output buffer is not large enough to contain the output buffer header, the <b>Status</b> member is set to STATUS_BUFFER_TOO_SMALL. If the output buffer is large enough to contain the output buffer header, but is not large enough to contain all the output arguments from the control method, the <b>Status</b> member is set to STATUS_BUFFER_OVERFLOW, and <i>OutputBuffer</i>-&gt;<b>Length</b> is set to the required length of the output buffer.</p>

<p>If the request succeeds, the <i>IoStatusBlock</i>-&gt;<b>Information</b> member is set to the number of bytes that is returned in the output buffer; otherwise, the <b>Information</b> member is set to zero.</p>

<p>If the request succeeds, <i>IoStatusBlock</i>-&gt;<b>Status</b> is set to STATUS_SUCCESS; otherwise, the <b>Status</b> member is set to an error code. If the output buffer is not large enough to contain the output buffer header, the <b>Status</b> member is set to STATUS_BUFFER_TOO_SMALL. If the output buffer is large enough to contain the output buffer header, but is not large enough to contain all the output arguments from the control method, the <b>Status</b> member is set to STATUS_BUFFER_OVERFLOW, and <i>OutputBuffer</i>-&gt;<b>Length</b> is set to the required length of the output buffer.</p>

<p>If the request succeeds, the <i>IoStatusBlock</i>-&gt;<b>Information</b> member is set to the number of bytes that is returned in the output buffer; otherwise, the <b>Information</b> member is set to zero.</p>

<p>If the request succeeds, <i>IoStatusBlock</i>-&gt;<b>Status</b> is set to STATUS_SUCCESS; otherwise, the <b>Status</b> member is set to an error code. If the output buffer is not large enough to contain the output buffer header, the <b>Status</b> member is set to STATUS_BUFFER_TOO_SMALL. If the output buffer is large enough to contain the output buffer header, but is not large enough to contain all the output arguments from the control method, the <b>Status</b> member is set to STATUS_BUFFER_OVERFLOW, and <i>OutputBuffer</i>-&gt;<b>Length</b> is set to the required length of the output buffer.</p>

<p>If the request succeeds, the <i>IoStatusBlock</i>-&gt;<b>Information</b> member is set to the number of bytes that is returned in the output buffer; otherwise, the <b>Information</b> member is set to zero.</p>

<p>If the request succeeds, <i>IoStatusBlock</i>-&gt;<b>Status</b> is set to STATUS_SUCCESS; otherwise, the <b>Status</b> member is set to an error code. If the output buffer is not large enough to contain the output buffer header, the <b>Status</b> member is set to STATUS_BUFFER_TOO_SMALL. If the output buffer is large enough to contain the output buffer header, but is not large enough to contain all the output arguments from the control method, the <b>Status</b> member is set to STATUS_BUFFER_OVERFLOW, and <i>OutputBuffer</i>-&gt;<b>Length</b> is set to the required length of the output buffer.</p>

<p>If the request succeeds, the <i>IoStatusBlock</i>-&gt;<b>Information</b> member is set to the number of bytes that is returned in the output buffer; otherwise, the <b>Information</b> member is set to zero.</p>

<p>If the request succeeds, <i>IoStatusBlock</i>-&gt;<b>Status</b> is set to STATUS_SUCCESS; otherwise, the <b>Status</b> member is set to an error code. If the output buffer is not large enough to contain the output buffer header, the <b>Status</b> member is set to STATUS_BUFFER_TOO_SMALL. If the output buffer is large enough to contain the output buffer header, but is not large enough to contain all the output arguments from the control method, the <b>Status</b> member is set to STATUS_BUFFER_OVERFLOW, and <i>OutputBuffer</i>-&gt;<b>Length</b> is set to the required length of the output buffer.</p>

<p>If the request succeeds, the <i>IoStatusBlock</i>-&gt;<b>Information</b> member is set to the number of bytes that is returned in the output buffer; otherwise, the <b>Information</b> member is set to zero.</p>

## -remarks
<p>A driver for a device can use IOCTL_ACPI_EVAL_METHOD to synchronously evaluate a control method that the device supports. For example, if the device is named 'ABCD' in an ACPI namespace and the 'ABCD' device supports a method named '_FOO,' this IOCTL can be used to evaluate control method '_FOO' by sending the sending the request to the 'ABCD' device and supplying the control method name '_FOO.' </p>

<p>IOCTL_ACPI_EVAL_METHOD supports the following types of input buffer structures:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>

<p>The output arguments from the control method are returned in the variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536123">ACPI_EVAL_OUTPUT_BUFFER</a> structure that is supplied by the <i>OutBuffer</i> pointer. The ACPI_EVAL_OUTPUT_BUFFER includes an array of variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536125">ACPI_METHOD_ARGUMENT</a> structures, each of which returns an output argument.</p>

<p>For more information about how to synchronously evaluate control methods, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/acpi/evaluating-acpi-control-methods-synchronously">Evaluating ACPI Control Methods Synchronously</a>.</p>

<p>Starting with Windows Server 2008 and Windows Vista, a driver can also use an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536149">IOCTL_ACPI_EVAL_METHOD_EX</a> request to synchronously evaluate a control method that is not an immediate child object of a device.</p>

<p>For information about how to evaluate an ACPI control method asynchronously starting on Windows Server 2008 and Windows Vista, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536145">IOCTL_ACPI_ASYNC_EVAL_METHOD</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536146">IOCTL_ACPI_ASYNC_EVAL_METHOD_EX</a>.</p>

<p>IOCTL_ACPI_EVAL_METHOD can be used only at IRQL &lt; DISPATCH_LEVEL.</p>

<p>A driver for a device can use IOCTL_ACPI_EVAL_METHOD to synchronously evaluate a control method that the device supports. For example, if the device is named 'ABCD' in an ACPI namespace and the 'ABCD' device supports a method named '_FOO,' this IOCTL can be used to evaluate control method '_FOO' by sending the sending the request to the 'ABCD' device and supplying the control method name '_FOO.' </p>

<p>IOCTL_ACPI_EVAL_METHOD supports the following types of input buffer structures:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>

<p>The output arguments from the control method are returned in the variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536123">ACPI_EVAL_OUTPUT_BUFFER</a> structure that is supplied by the <i>OutBuffer</i> pointer. The ACPI_EVAL_OUTPUT_BUFFER includes an array of variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536125">ACPI_METHOD_ARGUMENT</a> structures, each of which returns an output argument.</p>

<p>For more information about how to synchronously evaluate control methods, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/acpi/evaluating-acpi-control-methods-synchronously">Evaluating ACPI Control Methods Synchronously</a>.</p>

<p>Starting with Windows Server 2008 and Windows Vista, a driver can also use an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536149">IOCTL_ACPI_EVAL_METHOD_EX</a> request to synchronously evaluate a control method that is not an immediate child object of a device.</p>

<p>For information about how to evaluate an ACPI control method asynchronously starting on Windows Server 2008 and Windows Vista, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536145">IOCTL_ACPI_ASYNC_EVAL_METHOD</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536146">IOCTL_ACPI_ASYNC_EVAL_METHOD_EX</a>.</p>

<p>IOCTL_ACPI_EVAL_METHOD can be used only at IRQL &lt; DISPATCH_LEVEL.</p>

<p>A driver for a device can use IOCTL_ACPI_EVAL_METHOD to synchronously evaluate a control method that the device supports. For example, if the device is named 'ABCD' in an ACPI namespace and the 'ABCD' device supports a method named '_FOO,' this IOCTL can be used to evaluate control method '_FOO' by sending the sending the request to the 'ABCD' device and supplying the control method name '_FOO.' </p>

<p>IOCTL_ACPI_EVAL_METHOD supports the following types of input buffer structures:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>

<p>The output arguments from the control method are returned in the variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536123">ACPI_EVAL_OUTPUT_BUFFER</a> structure that is supplied by the <i>OutBuffer</i> pointer. The ACPI_EVAL_OUTPUT_BUFFER includes an array of variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536125">ACPI_METHOD_ARGUMENT</a> structures, each of which returns an output argument.</p>

<p>For more information about how to synchronously evaluate control methods, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/acpi/evaluating-acpi-control-methods-synchronously">Evaluating ACPI Control Methods Synchronously</a>.</p>

<p>Starting with Windows Server 2008 and Windows Vista, a driver can also use an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536149">IOCTL_ACPI_EVAL_METHOD_EX</a> request to synchronously evaluate a control method that is not an immediate child object of a device.</p>

<p>For information about how to evaluate an ACPI control method asynchronously starting on Windows Server 2008 and Windows Vista, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536145">IOCTL_ACPI_ASYNC_EVAL_METHOD</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536146">IOCTL_ACPI_ASYNC_EVAL_METHOD_EX</a>.</p>

<p>IOCTL_ACPI_EVAL_METHOD can be used only at IRQL &lt; DISPATCH_LEVEL.</p>

<p>A driver for a device can use IOCTL_ACPI_EVAL_METHOD to synchronously evaluate a control method that the device supports. For example, if the device is named 'ABCD' in an ACPI namespace and the 'ABCD' device supports a method named '_FOO,' this IOCTL can be used to evaluate control method '_FOO' by sending the sending the request to the 'ABCD' device and supplying the control method name '_FOO.' </p>

<p>IOCTL_ACPI_EVAL_METHOD supports the following types of input buffer structures:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>

<p>The output arguments from the control method are returned in the variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536123">ACPI_EVAL_OUTPUT_BUFFER</a> structure that is supplied by the <i>OutBuffer</i> pointer. The ACPI_EVAL_OUTPUT_BUFFER includes an array of variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536125">ACPI_METHOD_ARGUMENT</a> structures, each of which returns an output argument.</p>

<p>For more information about how to synchronously evaluate control methods, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/acpi/evaluating-acpi-control-methods-synchronously">Evaluating ACPI Control Methods Synchronously</a>.</p>

<p>Starting with Windows Server 2008 and Windows Vista, a driver can also use an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536149">IOCTL_ACPI_EVAL_METHOD_EX</a> request to synchronously evaluate a control method that is not an immediate child object of a device.</p>

<p>For information about how to evaluate an ACPI control method asynchronously starting on Windows Server 2008 and Windows Vista, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536145">IOCTL_ACPI_ASYNC_EVAL_METHOD</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536146">IOCTL_ACPI_ASYNC_EVAL_METHOD_EX</a>.</p>

<p>IOCTL_ACPI_EVAL_METHOD can be used only at IRQL &lt; DISPATCH_LEVEL.</p>

<p>A driver for a device can use IOCTL_ACPI_EVAL_METHOD to synchronously evaluate a control method that the device supports. For example, if the device is named 'ABCD' in an ACPI namespace and the 'ABCD' device supports a method named '_FOO,' this IOCTL can be used to evaluate control method '_FOO' by sending the sending the request to the 'ABCD' device and supplying the control method name '_FOO.' </p>

<p>IOCTL_ACPI_EVAL_METHOD supports the following types of input buffer structures:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>

<p>The output arguments from the control method are returned in the variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536123">ACPI_EVAL_OUTPUT_BUFFER</a> structure that is supplied by the <i>OutBuffer</i> pointer. The ACPI_EVAL_OUTPUT_BUFFER includes an array of variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536125">ACPI_METHOD_ARGUMENT</a> structures, each of which returns an output argument.</p>

<p>For more information about how to synchronously evaluate control methods, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/acpi/evaluating-acpi-control-methods-synchronously">Evaluating ACPI Control Methods Synchronously</a>.</p>

<p>Starting with Windows Server 2008 and Windows Vista, a driver can also use an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536149">IOCTL_ACPI_EVAL_METHOD_EX</a> request to synchronously evaluate a control method that is not an immediate child object of a device.</p>

<p>For information about how to evaluate an ACPI control method asynchronously starting on Windows Server 2008 and Windows Vista, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536145">IOCTL_ACPI_ASYNC_EVAL_METHOD</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536146">IOCTL_ACPI_ASYNC_EVAL_METHOD_EX</a>.</p>

<p>IOCTL_ACPI_EVAL_METHOD can be used only at IRQL &lt; DISPATCH_LEVEL.</p>

<p>A driver for a device can use IOCTL_ACPI_EVAL_METHOD to synchronously evaluate a control method that the device supports. For example, if the device is named 'ABCD' in an ACPI namespace and the 'ABCD' device supports a method named '_FOO,' this IOCTL can be used to evaluate control method '_FOO' by sending the sending the request to the 'ABCD' device and supplying the control method name '_FOO.' </p>

<p>IOCTL_ACPI_EVAL_METHOD supports the following types of input buffer structures:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</p>

<p>The output arguments from the control method are returned in the variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536123">ACPI_EVAL_OUTPUT_BUFFER</a> structure that is supplied by the <i>OutBuffer</i> pointer. The ACPI_EVAL_OUTPUT_BUFFER includes an array of variable-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff536125">ACPI_METHOD_ARGUMENT</a> structures, each of which returns an output argument.</p>

<p>For more information about how to synchronously evaluate control methods, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/acpi/evaluating-acpi-control-methods-synchronously">Evaluating ACPI Control Methods Synchronously</a>.</p>

<p>Starting with Windows Server 2008 and Windows Vista, a driver can also use an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536149">IOCTL_ACPI_EVAL_METHOD_EX</a> request to synchronously evaluate a control method that is not an immediate child object of a device.</p>

<p>For information about how to evaluate an ACPI control method asynchronously starting on Windows Server 2008 and Windows Vista, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536145">IOCTL_ACPI_ASYNC_EVAL_METHOD</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536146">IOCTL_ACPI_ASYNC_EVAL_METHOD_EX</a>.</p>

<p>IOCTL_ACPI_EVAL_METHOD can be used only at IRQL &lt; DISPATCH_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Acpiioct.h (include Acpiioct.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536115">ACPI_EVAL_INPUT_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536116">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536119">ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536121">ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536123">ACPI_EVAL_OUTPUT_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536125">ACPI_METHOD_ARGUMENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536145">IOCTL_ACPI_ASYNC_EVAL_METHOD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536146">IOCTL_ACPI_ASYNC_EVAL_METHOD_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536149">IOCTL_ACPI_EVAL_METHOD_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [acpi\acpi]:%20IOCTL_ACPI_EVAL_METHOD control code%20 RELEASE:%20(11/16/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
