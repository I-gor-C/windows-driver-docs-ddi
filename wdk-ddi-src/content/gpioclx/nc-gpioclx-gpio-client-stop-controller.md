---
UID: NC.gpioclx.GPIO_CLIENT_STOP_CONTROLLER
title: GPIO_CLIENT_STOP_CONTROLLER
author: windows-driver-content
description: The CLIENT_StopController event callback function performs operations that are needed to prepare the general-purpose I/O (GPIO) controller device to exit the D0 power state.
old-location: gpio\client_stopcontroller.htm
old-project: GPIO
ms.assetid: 4B1A33AC-E341-478E-8C1E-94F4473A191C
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
req.alt-api: CLIENT_StopController
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

# GPIO_CLIENT_STOP_CONTROLLER callback



## -description
<p>The <i>CLIENT_StopController</i> event callback function performs operations that are needed to prepare the general-purpose I/O (GPIO) controller device to exit the D0 power state.</p>


## -prototype

````
GPIO_CLIENT_STOP_CONTROLLER CLIENT_StopController;

NTSTATUS CLIENT_StopController(
  _In_ PVOID                  Context,
  _In_ BOOLEAN                SaveContext,
  _In_ WDF_POWER_DEVICE_STATE TargetState
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to the GPIO controller driver's <a href="https://msdn.microsoft.com/4BE99C71-9BA6-44E3-A54F-DE8C3440A474">device context</a>.</p>
</dd>

### -param <i>SaveContext</i> [in]

<dd>
<p>Whether the client driver should save the current hardware context of the GPIO controller device. If TRUE, the hardware context should be saved. If FALSE, the hardware context should not be saved. For more information, see Remarks.</p>
</dd>

### -param <i>TargetState</i> [in]

<dd>
<p>The target device power state. This parameter is a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552421">WDF_POWER_DEVICE_STATE</a> enumeration value that specifies the low-power state that the device is to enter when it exits the D0 power state. The GPIO controller driver can use this information to determine how to configure the controller device before it leaves D0.</p>
</dd>
</dl>

## -returns
<p>The <i>CLIENT_StopController</i> function returns STATUS_SUCCESS if the call is successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>This callback function is implemented by the GPIO controller driver. The GPIO framework extension (GpioClx) calls this function to prepare the GPIO controller device to be turned off or to transition to a low-power state. This callback function must perform any operations that are necessary before the device enters a low-power state, such as saving any information that the driver will need later after the device is restored to the D0 power state.</p>

<p>Typically, the <i>CLIENT_StopController</i> callback function configures the GPIO pins to a platform-specific initial state. For example, this function might configure all of the GPIO pins as inputs to prevent output transients from occurring when the GPIO controller device is turned off.</p>

<p>To register your driver's <i>CLIENT_StopController</i> callback function, call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439490">GPIO_CLX_RegisterClient</a> method. This method accepts, as an input parameter, a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh439479">GPIO_CLIENT_REGISTRATION_PACKET</a> structure that contains a <i>CLIENT_StopController</i> function pointer.</p>

<p>Although the <i>CLIENT_StopController</i> callback function is called at IRQL = PASSIVE_LEVEL, you should not make this function pageable. The <i>CLIENT_StopController</i> callback is in the critical timing path for restoring power to the devices in the hardware platform and, for performance reasons, it should not be delayed by page faults.</p>

<p>To define a <i>CLIENT_StopController</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>CLIENT_StopController</i> callback function that is named <code>MyEvtGpioStopController</code>, use the GPIO_CLIENT_STOP_CONTROLLER function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The GPIO_CLIENT_STOP_CONTROLLER function type is defined in the Gpioclx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the GPIO_CLIENT_STOP_CONTROLLER function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

<p>This callback function is implemented by the GPIO controller driver. The GPIO framework extension (GpioClx) calls this function to prepare the GPIO controller device to be turned off or to transition to a low-power state. This callback function must perform any operations that are necessary before the device enters a low-power state, such as saving any information that the driver will need later after the device is restored to the D0 power state.</p>

<p>Typically, the <i>CLIENT_StopController</i> callback function configures the GPIO pins to a platform-specific initial state. For example, this function might configure all of the GPIO pins as inputs to prevent output transients from occurring when the GPIO controller device is turned off.</p>

<p>To register your driver's <i>CLIENT_StopController</i> callback function, call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439490">GPIO_CLX_RegisterClient</a> method. This method accepts, as an input parameter, a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh439479">GPIO_CLIENT_REGISTRATION_PACKET</a> structure that contains a <i>CLIENT_StopController</i> function pointer.</p>

<p>Although the <i>CLIENT_StopController</i> callback function is called at IRQL = PASSIVE_LEVEL, you should not make this function pageable. The <i>CLIENT_StopController</i> callback is in the critical timing path for restoring power to the devices in the hardware platform and, for performance reasons, it should not be delayed by page faults.</p>

<p>To define a <i>CLIENT_StopController</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>CLIENT_StopController</i> callback function that is named <code>MyEvtGpioStopController</code>, use the GPIO_CLIENT_STOP_CONTROLLER function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The GPIO_CLIENT_STOP_CONTROLLER function type is defined in the Gpioclx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the GPIO_CLIENT_STOP_CONTROLLER function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439479">GPIO_CLIENT_REGISTRATION_PACKET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439490">GPIO_CLX_RegisterClient</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [GPIO\parports]:%20CLIENT_StopController callback function%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
