---
UID: NE.gpioclx._CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE
title: CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE
author: windows-driver-content
description: The CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE enumeration type indicates what type of attribute information the GPIO framework extension (GpioClx) is requesting from the GPIO controller driver.
old-location: gpio\client_controller_query_set_request_type.htm
ms.assetid: 050752CC-FBD6-4EB1-A17F-53C5C569E3FB
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: GPIO
req.header: gpioclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: PGNSS_V2UPL_NI_INFO, GNSS_V2UPL_NI_INFO, *PGNSS_V2UPL_NI_INFO
req.iface: 
---

# CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE enumeration



## -description
<p>The <b>CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE</b> enumeration type indicates what type of attribute information the GPIO framework extension (GpioClx) is requesting from the GPIO controller driver.</p>


## -syntax

````
typedef enum _CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE { 
  QueryBankPowerInformation,
  QueryBankInterruptBindingInformation,
  QueryControllerFunctionBankMappingInformation,
  QuerySetRequestMaximumType
} CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE;
````


## -enum-fields
<dl>

### -field <a id="QueryBankPowerInformation"></a><a id="querybankpowerinformation"></a><a id="QUERYBANKPOWERINFORMATION"></a><b>QueryBankPowerInformation</b>

<dd>
<p>Power attributes. For this attribute type, the <b>BankPowerInformation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh698238">CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</a> structure specifies a GPIO bank, and the <b>BankPowerInformation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh698239">CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</a> structure contains the power attributes of the specified bank.</p>
</dd>

### -field <a id="QueryBankInterruptBindingInformation"></a><a id="querybankinterruptbindinginformation"></a><a id="QUERYBANKINTERRUPTBINDINGINFORMATION"></a><b>QueryBankInterruptBindingInformation</b>

<dd>
<p>Interrupt-binding attributes. For this attribute type, the <b>BankInterruptBinding</b> member of the <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure contains the raw and translated hardware resources assigned to the GPIO controller, and the <b>BankInterruptBinding</b> member of the <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</b> structure describes the binding of interrupt resources to GPIO banks.</p>
</dd>

### -field <a id="QueryControllerFunctionBankMappingInformation"></a><a id="querycontrollerfunctionbankmappinginformation"></a><a id="QUERYCONTROLLERFUNCTIONBANKMAPPINGINFORMATION"></a><b>QueryControllerFunctionBankMappingInformation</b>

<dd>
<p>Function-mapping attributes. For this attribute type, the <b>ControllerFunctionBankMapping</b> member of the <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure specifies an I/O control request (IOCTL), and the <b>ControllerFunctionBankMapping</b> member of the <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</b> structure indicates which GPIO banks must be in the F0 (fully on) power state to handle the specified IOCTL.</p>
</dd>

### -field <a id="QuerySetRequestMaximumType"></a><a id="querysetrequestmaximumtype"></a><a id="QUERYSETREQUESTMAXIMUMTYPE"></a><b>QuerySetRequestMaximumType</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>
</dl>

## -remarks
<p>The <b>RequestType</b> member of the <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure is a value of type <b>CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE</b>. GpioClx sets this member to a  <b>CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE</b> enumeration constant to indicate what type of attribute information is requested. The <a href="https://msdn.microsoft.com/library/windows/hardware/hh698241">CLIENT_QuerySetControllerInformation</a> callback function takes a pointer to a <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure as an input parameter, and optionally takes a pointer to a <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</b> structure as an output parameter.</p>

<p>The <b>RequestType</b> member of the <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure is a value of type <b>CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE</b>. GpioClx sets this member to a  <b>CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE</b> enumeration constant to indicate what type of attribute information is requested. The <a href="https://msdn.microsoft.com/library/windows/hardware/hh698241">CLIENT_QuerySetControllerInformation</a> callback function takes a pointer to a <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure as an input parameter, and optionally takes a pointer to a <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</b> structure as an output parameter.</p>

<p>The <b>RequestType</b> member of the <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure is a value of type <b>CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE</b>. GpioClx sets this member to a  <b>CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE</b> enumeration constant to indicate what type of attribute information is requested. The <a href="https://msdn.microsoft.com/library/windows/hardware/hh698241">CLIENT_QuerySetControllerInformation</a> callback function takes a pointer to a <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure as an input parameter, and optionally takes a pointer to a <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</b> structure as an output parameter.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh698238">CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh698239">CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh698241">CLIENT_QuerySetControllerInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [GPIO\parports]:%20CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
