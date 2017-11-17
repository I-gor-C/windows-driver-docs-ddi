---
UID: NF.mcd.ChangerPerformDiagnostics
title: ChangerPerformDiagnostics
author: windows-driver-content
description: ChangerPerformDiagnostics performs diagnostic tests on the changer device.
old-location: storage\changerperformdiagnostics.htm
ms.assetid: 87767b2b-8ca3-4d19-8719-673562246a41
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: mcd.h
req.include-header: Mcd.h, Ntddchgr.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ChangerPerformDiagnostics
req.alt-loc: mcd.h
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
ms.keywords: ChangerPerformDiagnostics
req.iface: 
---

# ChangerPerformDiagnostics function



## -description
<p><b>ChangerPerformDiagnostics</b> performs diagnostic tests on the changer device.</p>


## -syntax

````
NTSTATUS ChangerPerformDiagnostics(
  _In_  PDEVICE_OBJECT                    DeviceObject,
  _Out_ PWMI_CHANGER_PROBLEM_DEVICE_ERROR ChangerDeviceError
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object that represents the changer.</p>
</dd>

### -param <i>ChangerDeviceError</i> [out]

<dd>
<p>Pointer to the buffer of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff568029">WMI_CHANGER_PROBLEM_DEVICE_ERROR</a> in which the minidriver returns the diagnostic information.</p>
</dd>
</dl>

## -returns
<p><b>ChangerPerformDiagnostics</b> returns the status returned by the system port driver or one of the following values:
      </p>

<p>STATUS_SUCCESS</p>

<p>STATUS_INSUFFICIENT_RESOURCES</p>

<p>STATUS_BUFFER_TOO_SMALL</p>

## -remarks
<p><b>ChangerPerformDiagnostics</b> routine performs diagnostic tests on the changer device, and reports the problem to the caller. The kind of tests performed depends on the diagnostics support provided by the device. </p>

<p><b>ChangerPerformDiagnostics</b> routine performs diagnostic tests on the changer device, and reports the problem to the caller. The kind of tests performed depends on the diagnostics support provided by the device. </p>

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
<dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568029">WMI_CHANGER_PROBLEM_DEVICE_ERROR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551453">CHANGER_DEVICE_PROBLEM_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20ChangerPerformDiagnostics function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
