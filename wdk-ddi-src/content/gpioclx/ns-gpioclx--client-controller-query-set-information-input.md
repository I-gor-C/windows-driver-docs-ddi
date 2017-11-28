---
UID: NS.gpioclx._CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT
title: CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT
author: windows-driver-content
description: The CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT structure contains a request for the hardware attributes of the general-purpose I/O (GPIO) controller.
old-location: gpio\client_controller_query_set_information_input.htm
old-project: GPIO
ms.assetid: C4AA60FF-03AD-444F-B897-654B787B5F86
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.keywords: CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gpioclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT
req.alt-loc: Gpioclx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT structure



## -description
<p>The <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure contains a request for the hardware attributes of the general-purpose I/O (GPIO) controller.</p>


## -syntax

````
typedef struct _CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT {
  CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE RequestType;
  USHORT                                   Size;
  ULONG                                    Flags;
  union {
    struct {
      BANK_ID BankId;
    } BankPowerInformation;
    struct {
      WDFCMRESLIST ResourcesTranslated;
      WDFCMRESLIST ResourcesRaw;
      USHORT       TotalBanks;
    } BankInterruptBinding;
    struct {
      PVOID  InputBuffer;
      SIZE_T InputBufferSize;
      SIZE_T OutputBufferSize;
      USHORT TotalBanks;
    } ControllerFunctionBankMapping;
  };
} CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT, *PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT;
````


## -struct-fields
<dl>

### -field <b>RequestType</b>

<dd>
<p>The type of attribute information that is being requested. This member is set to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh698240">CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE</a> enumeration value.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Specifies the size, in bytes, of the <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A set of flag bits that supply additional information about the type of attribute request indicated by the <b>RequestType</b> member. No flags are currently defined for the <b>Flags</b> member.</p>
</dd>

### -field ( <i>unnamed union</i> )

<dd>
<p>A union of members that contain input information for the various types of attribute requests. The <b>RequestType</b> member determines which member of this union is used. The following table shows the union member that corresponds to each valid <b>RequestType</b> value.</p>
<table>
<tr>
<th><b>RequestType</b> value</th>
<th>Union member</th>
</tr>
<tr>
<td><b>QueryBankPowerInformation</b></td>
<td><b>BankPowerInformation</b></td>
</tr>
<tr>
<td><b>QueryBankInterruptBindingInformation</b></td>
<td><b>BankInterruptBinding</b></td>
</tr>
<tr>
<td><b>QueryControllerFunctionBankMappingInformation</b></td>
<td><b>ControllerFunctionBankMapping</b></td>
</tr>
</table>
<p> </p>
<dl>

### -field <b>BankPowerInformation</b>

<dd>
<p>A structure that contains information about the GPIO bank whose power attributes are being requested.</p>
<dl>

### -field <b>BankId</b>

<dd>
<p>The identifier for a bank of GPIO pins. If M is the number of banks in the GPIO controller, <b>BankId</b> is an integer in the range 0 to M–1. The GPIO framework extension (GpioClx) previously obtained the number of banks in the controller from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439399">CLIENT_QueryControllerBasicInformation</a> event callback function. For more information, see Remarks in <a href="https://msdn.microsoft.com/library/windows/hardware/hh439358">CLIENT_CONTROLLER_BASIC_INFORMATION</a>.</p>
</dd>
</dl>
</dd>

### -field <b>BankInterruptBinding</b>

<dd>
<p>A structure that contains information about the interrupt resources that are assigned to the GPIO controller.</p>
<dl>

### -field <b>ResourcesTranslated</b>

<dd>
<p>A handle to a framework resource-list object that identifies the translated hardware resources that the Plug and Play manager has assigned to the device.</p>
</dd>

### -field <b>ResourcesRaw</b>

<dd>
<p>A handle to a framework resource-list object that identifies the raw hardware resources that the Plug and Play manager has assigned to the device.</p>
</dd>

### -field <b>TotalBanks</b>

<dd>
<p>The number of banks in the GPIO controller. This member indicates the expected length of the <b>BankInterruptBinding.ResourceMapping</b> array in the caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/hh698239">CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</a> structure, if the caller supplies a non-NULL pointer to this structure.</p>
</dd>
</dl>
</dd>

### -field <b>ControllerFunctionBankMapping</b>

<dd>
<p>A structure that contains information about an I/O control request (IOCTL).</p>
<dl>

### -field <b>InputBuffer</b>

<dd>
<p>A pointer to the input buffer for the IOCTL.</p>
</dd>

### -field <b>InputBufferSize</b>

<dd>
<p>The size, in bytes, of the input buffer for the IOCTL.</p>
</dd>

### -field <b>OutputBufferSize</b>

<dd>
<p>The size, in bytes, of the output buffer for the IOCTL.</p>
</dd>

### -field <b>TotalBanks</b>

<dd>
<p>The number of banks in the GPIO controller. This member indicates the expected length of the <b>ControllerFunctionBankMapping.Mapping</b> array in the caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/hh698239">CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</a> structure, if the caller supplies a non-NULL pointer to this structure.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <i>InputBuffer</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh698241">CLIENT_QuerySetControllerInformation</a> function is a pointer to a <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Gpioclx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439399">CLIENT_QueryControllerBasicInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh698241">CLIENT_QuerySetControllerInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439358">CLIENT_CONTROLLER_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh698239">CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [GPIO\parports]:%20CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
