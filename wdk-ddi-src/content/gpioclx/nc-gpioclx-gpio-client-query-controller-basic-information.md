---
UID: NC.gpioclx.GPIO_CLIENT_QUERY_CONTROLLER_BASIC_INFORMATION
title: GPIO_CLIENT_QUERY_CONTROLLER_BASIC_INFORMATION
author: windows-driver-content
description: The CLIENT_QueryControllerBasicInformation event callback function retrieves the hardware attributes of the general-purpose I/O (GPIO) controller.
old-location: gpio\client_querycontrollerbasicinformation.htm
old-project: GPIO
ms.assetid: 5674317C-6785-46F5-880F-71FAF2CD3C64
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.keywords: PGNSS_V2UPL_NI_INFO, GNSS_V2UPL_NI_INFO, *PGNSS_V2UPL_NI_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: gpioclx.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CLIENT_QueryControllerBasicInformation
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
req.irql: Called at PASSIVE_LEVEL.
req.iface: 
---

# GPIO_CLIENT_QUERY_CONTROLLER_BASIC_INFORMATION callback



## -description
<p>The <i>CLIENT_QueryControllerBasicInformation</i> event callback function retrieves the hardware attributes of the general-purpose I/O (GPIO) controller.</p>


## -prototype

````
GPIO_CLIENT_QUERY_CONTROLLER_BASIC_INFORMATION CLIENT_QueryControllerBasicInformation;

NTSTATUS CLIENT_QueryControllerBasicInformation(
  _In_  PVOID                                Context,
  _Out_ PCLIENT_CONTROLLER_BASIC_INFORMATION Information
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to the GPIO controller driver's <a href="https://msdn.microsoft.com/4BE99C71-9BA6-44E3-A54F-DE8C3440A474">device context</a>.</p>
</dd>

### -param <i>Information</i> [out]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/hh439358">CLIENT_CONTROLLER_BASIC_INFORMATION</a> structure. The <i>CLIENT_QueryControllerBasicInformation</i> function writes the GPIO controller hardware attributes and configuration information into this structure.</p>
</dd>
</dl>

## -returns
<p>The <i>CLIENT_QueryControllerBasicInformation</i> function returns STATUS_SUCCESS if the call is successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>This callback function is implemented by the GPIO controller driver. The GPIO framework extension (GpioClx) calls this function.</p>

<p>The <i>CLIENT_QueryControllerBasicInformation</i> callback function should set all members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439358">CLIENT_CONTROLLER_BASIC_INFORMATION</a> structure, including the <b>Version</b> and <b>Size</b> members. GpioClx does not initialize the <b>Size</b> member before calling this function, but the buffer that the <i>Information</i> parameter points to is guaranteed to be large enough to contain the version of this structure that the GPIO controller driver uses.</p>

<p>To register your driver's <i>CLIENT_QueryControllerBasicInformation</i> callback function, call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439490">GPIO_CLX_RegisterClient</a> method. This method accepts, as an input parameter, a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh439479">GPIO_CLIENT_REGISTRATION_PACKET</a> structure that contains a <i>CLIENT_QueryControllerBasicInformation</i> function pointer.</p>

<p>To define a <i>CLIENT_QueryControllerBasicInformation</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>CLIENT_QueryControllerBasicInformation</i> callback function that is named <code>MyEvtGpioQueryControllerBasicInformation</code>, use the GPIO_CLIENT_QUERY_CONTROLLER_BASIC_INFORMATION function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The GPIO_CLIENT_QUERY_CONTROLLER_BASIC_INFORMATION function type is defined in the Gpioclx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the GPIO_CLIENT_QUERY_CONTROLLER_BASIC_INFORMATION function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Called at PASSIVE_LEVEL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439358">CLIENT_CONTROLLER_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439479">GPIO_CLIENT_REGISTRATION_PACKET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439490">GPIO_CLX_RegisterClient</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [GPIO\parports]:%20CLIENT_QueryControllerBasicInformation callback function%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
