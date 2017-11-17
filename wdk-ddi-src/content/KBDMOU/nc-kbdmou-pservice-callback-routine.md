---
UID: NC.kbdmou.PSERVICE_CALLBACK_ROUTINE
title: PSERVICE_CALLBACK_ROUTINE
author: windows-driver-content
description: A function driver calls the class service callback in its ISR dispatch completion routine. The class service callback transfers input data from the input data buffer of a device to the class data queue.
old-location: hid\kbdclass_class_service_callback_routine.htm
ms.assetid: 78ae2a98-bebd-43ee-b016-2f619c3135ca
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: hid
req.header: kbdmou.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClassServiceCallback
req.alt-loc: kbdmou.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
ms.keywords: MSiSCSI_SessionStatistics, MSiSCSI_SessionStatistics, *PMSiSCSI_SessionStatistics
req.iface: 
---

# PSERVICE_CALLBACK_ROUTINE callback



## -description
<p>A function driver calls the class service callback in its ISR dispatch completion routine. The class service callback transfers input data from the input data buffer of a device to the class data queue. </p>


## -prototype

````
PSERVICE_CALLBACK_ROUTINE ClassServiceCallback;

VOID ClassServiceCallback(
  _In_    PVOID NormalContext,
  _In_    PVOID SystemArgument1,
  _In_    PVOID SystemArgument2,
  _Inout_ PVOID SystemArgument3
)
{ ... }
````


## -parameters
<dl>

### -param <i>NormalContext</i> [in]

<dd>
<p>Pointer to the class device object.</p>
</dd>

### -param <i>SystemArgument1</i> [in]

<dd>
<p>Pointer to the first keyboard input data packet in the input data buffer of the port device.</p>
</dd>

### -param <i>SystemArgument2</i> [in]

<dd>
<p>Pointer to the keyboard input data packet that immediately follows the last data packet in the input data buffer of the port device.</p>
</dd>

### -param <i>SystemArgument3</i> [in, out]

<dd>
<p>Pointer to the number of keyboard input data packets that are transferred by the routine.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p><b>Keyboard Class Service Callback</b></p>

<p>Here is the definition of the  keyboard class service callback routine.</p>

<p>Kbdclass uses an <a href="https://msdn.microsoft.com/library/windows/hardware/ff541273">IOCTL_INTERNAL_KEYBOARD_CONNECT</a> request to connect its class service callback to a keyboard device. In this call, the driver sets  its implementation in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff538370">CONNECT_DATA</a> structure.</p>

<p><b>KeyboardClassServiceCallback</b> transfers input data from the input buffer of the device to the class data queue. This routine is called by the ISR dispatch completion routine of the function driver.</p>

<p><b>KeyboardClassServiceCallback</b> can be supplemented by a filter service callback that is provided by an upper-level keyboard filter driver. A filter service callback filters the keyboard data that is transferred to the class data queue. For example, the filter service callback can delete, transform, or insert data. <a href="http://go.microsoft.com/fwlink/p/?linkid=256125">Kbfiltr</a>, the sample filter driver in code gallery, includes <b>KbFilter_ServiceCallback</b>, which is a template for a keyboard filter service callback.</p>

<p><b>Mouse Class Service Callback</b></p>

<p>Here is the <b>MouseClassServiceCallback</b> routine is the class service callback routine that is provided by Mouclass. The driver uses an <a href="https://msdn.microsoft.com/library/windows/hardware/ff541294">IOCTL_INTERNAL_MOUSE_CONNECT</a> request to connect its class service callback to a mouse device. In this call, the driver sets  its implementation in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff538370">CONNECT_DATA</a> structure.</p>

<p>
<pre class="syntax" xml:space="preserve"><code>
/*
DeviceObject [in] 
Pointer to the class device object.

InputDataStart [in] 
Pointer to the first mouse input data packet in the input buffer of the port device.

InputDataEnd [in] 
Pointer to the mouse input data packet that immediately follows the last data packet in the input data buffer of the port device.

InputDataConsumed [in, out] 
Pointer to the number of mouse input data packets that are transferred by the routine.

*/
VOID MouseClassServiceCallback(
  _In_    PDEVICE_OBJECT    DeviceObject,
  _In_    PMOUSE_INPUT_DATA InputDataStart,
  _In_    PMOUSE_INPUT_DATA InputDataEnd,
  _Inout_ PULONG            InputDataConsumed
);
);
</code></pre>
</p>

<p><b>MouseClassServiceCallback</b> transfers input data from the input buffer of the device to the class data queue. This routine is called by the ISR dispatch completion routine of the function driver.</p>

<p><b>MouseClassServiceCallback</b> can be supplemented by a filter service callback that is provided by an upper-level mouse filter driver. A filter service callback can filter the mouse data that is transferred to the class data queue. For example, the filter service callback can delete, transform, or insert data. <a href="http://go.microsoft.com/fwlink/p/?linkid=256135">Moufiltr</a>, the sample filter driver in the WDK, includes <b>MouFilter_ServiceCallback</b>, which is a template for a filter service callback.</p>

<p><b>Keyboard Class Service Callback</b></p>

<p>Here is the definition of the  keyboard class service callback routine.</p>

<p>Kbdclass uses an <a href="https://msdn.microsoft.com/library/windows/hardware/ff541273">IOCTL_INTERNAL_KEYBOARD_CONNECT</a> request to connect its class service callback to a keyboard device. In this call, the driver sets  its implementation in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff538370">CONNECT_DATA</a> structure.</p>

<p><b>KeyboardClassServiceCallback</b> transfers input data from the input buffer of the device to the class data queue. This routine is called by the ISR dispatch completion routine of the function driver.</p>

<p><b>KeyboardClassServiceCallback</b> can be supplemented by a filter service callback that is provided by an upper-level keyboard filter driver. A filter service callback filters the keyboard data that is transferred to the class data queue. For example, the filter service callback can delete, transform, or insert data. <a href="http://go.microsoft.com/fwlink/p/?linkid=256125">Kbfiltr</a>, the sample filter driver in code gallery, includes <b>KbFilter_ServiceCallback</b>, which is a template for a keyboard filter service callback.</p>

<p><b>Mouse Class Service Callback</b></p>

<p>Here is the <b>MouseClassServiceCallback</b> routine is the class service callback routine that is provided by Mouclass. The driver uses an <a href="https://msdn.microsoft.com/library/windows/hardware/ff541294">IOCTL_INTERNAL_MOUSE_CONNECT</a> request to connect its class service callback to a mouse device. In this call, the driver sets  its implementation in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff538370">CONNECT_DATA</a> structure.</p>

<p>
<pre class="syntax" xml:space="preserve"><code>
/*
DeviceObject [in] 
Pointer to the class device object.

InputDataStart [in] 
Pointer to the first mouse input data packet in the input buffer of the port device.

InputDataEnd [in] 
Pointer to the mouse input data packet that immediately follows the last data packet in the input data buffer of the port device.

InputDataConsumed [in, out] 
Pointer to the number of mouse input data packets that are transferred by the routine.

*/
VOID MouseClassServiceCallback(
  _In_    PDEVICE_OBJECT    DeviceObject,
  _In_    PMOUSE_INPUT_DATA InputDataStart,
  _In_    PMOUSE_INPUT_DATA InputDataEnd,
  _Inout_ PULONG            InputDataConsumed
);
);
</code></pre>
</p>

<p><b>MouseClassServiceCallback</b> transfers input data from the input buffer of the device to the class data queue. This routine is called by the ISR dispatch completion routine of the function driver.</p>

<p><b>MouseClassServiceCallback</b> can be supplemented by a filter service callback that is provided by an upper-level mouse filter driver. A filter service callback can filter the mouse data that is transferred to the class data queue. For example, the filter service callback can delete, transform, or insert data. <a href="http://go.microsoft.com/fwlink/p/?linkid=256135">Moufiltr</a>, the sample filter driver in the WDK, includes <b>MouFilter_ServiceCallback</b>, which is a template for a filter service callback.</p>

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
<dt>Kbdmou.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542337">KEYBOARD_INPUT_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542403">MOUSE_INPUT_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538370">CONNECT_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20PSERVICE_CALLBACK_ROUTINE callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
