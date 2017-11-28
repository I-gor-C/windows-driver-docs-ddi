---
UID: NS.mcd._MCD_INIT_DATA
title: MCD_INIT_DATA
author: windows-driver-content
description: The changer miniclass driver fills the MCD_INIT_DATA structure with pointers to its internal command processing routines and passes them to the changer class driver.
old-location: storage\mcd_init_data.htm
old-project: storage
ms.assetid: 4fc4c36f-a2ad-4b9f-a30b-e7ed600c38e9
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MCD_INIT_DATA, MCD_INIT_DATA, *PMCD_INIT_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mcd.h
req.include-header: Mcd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MCD_INIT_DATA
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# MCD_INIT_DATA structure



## -description
<p>The changer miniclass driver fills the MCD_INIT_DATA structure with pointers to its internal command processing routines and passes them to the changer class driver. </p>


## -syntax

````
typedef struct _MCD_INIT_DATA {
  ULONG                       InitDataSize;
  CHANGER_EXTENSION_SIZE      ChangerAdditionalExtensionSize;
  CHANGER_INITIALIZE          ChangerInitialize;
  CHANGER_ERROR_ROUTINE       ChangerError;
  CHANGER_PERFORM_DIAGNOSTICS ChangerPerformDiagnostics;
  CHANGER_COMMAND_ROUTINE     ChangerGetParameters;
  CHANGER_COMMAND_ROUTINE     ChangerGetStatus;
  CHANGER_COMMAND_ROUTINE     ChangerGetProductData;
  CHANGER_COMMAND_ROUTINE     ChangerSetAccess;
  CHANGER_COMMAND_ROUTINE     ChangerGetElementStatus;
  CHANGER_COMMAND_ROUTINE     ChangerInitializeElementStatus;
  CHANGER_COMMAND_ROUTINE     ChangerSetPosition;
  CHANGER_COMMAND_ROUTINE     ChangerExchangeMedium;
  CHANGER_COMMAND_ROUTINE     ChangerMoveMedium;
  CHANGER_COMMAND_ROUTINE     ChangerReinitializeUnit;
  CHANGER_COMMAND_ROUTINE     ChangerQueryVolumeTags;
} MCD_INIT_DATA, *PMCD_INIT_DATA;
````


## -struct-fields
<dl>

### -field <b>InitDataSize</b>

<dd>
<p>Size of this structure in bytes. </p>
</dd>

### -field <b>ChangerAdditionalExtensionSize</b>

<dd>
<p>Pointer to changer miniclass driver routine that returns the number of bytes the changer miniclass driver requires to store device-specific information in the device extension. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
ULONG
(*CHANGER_EXTENSION_SIZE)(
  IN VOID
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerInitialize</b>

<dd>
<p>Pointer to changer miniclass driver routine that does miniclass driver-specific initialization and readies the changer to receive other requests. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef 
NTSTATUS
(*CHANGER_INITIALIZE)(
  IN PDEVICE_OBJECT  DeviceObject
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerError</b>

<dd>
<p>Pointer to changer miniclass driver routine that does device-specific error processing. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
VOID
(*CHANGER_ERROR_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PSCSI_REQUEST_BLOCK  Srb,
  IN NTSTATUS  *Status,
  IN BOOLEAN  *Retry
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerPerformDiagnostics</b>

<dd>
<p>Pointer to changer miniclass driver routine that performs diagnostic tests on the device. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef 
NTSTATUS
(*CHANGER_PERFORM_DIAGNOSTICS)(
  IN PDEVICE_OBJECT  DeviceObject,
  OUT PWMI_CHANGER_PROBLEM_DEVICE_ERROR  changerDeviceError
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerGetParameters</b>

<dd>
<p>Pointer to changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559399">IOCTL_CHANGER_GET_PARAMETERS</a>. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerGetStatus</b>

<dd>
<p>Pointer to changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559405">IOCTL_CHANGER_GET_STATUS</a>. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerGetProductData</b>

<dd>
<p>Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559402">IOCTL_CHANGER_GET_PRODUCT_DATA</a>. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerSetAccess</b>

<dd>
<p>Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559422">IOCTL_CHANGER_SET_ACCESS</a>. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerGetElementStatus</b>

<dd>
<p>Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559396">IOCTL_CHANGER_GET_ELEMENT_STATUS</a>. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerInitializeElementStatus</b>

<dd>
<p>Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559409">IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS</a>. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerSetPosition</b>

<dd>
<p>Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559425">IOCTL_CHANGER_SET_POSITION</a>. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerExchangeMedium</b>

<dd>
<p>Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559391">IOCTL_CHANGER_EXCHANGE_MEDIUM</a>. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerMoveMedium</b>

<dd>
<p>Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559410">IOCTL_CHANGER_MOVE_MEDIUM</a>. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerReinitializeUnit</b>

<dd>
<p>Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559419">IOCTL_CHANGER_REINITIALIZE_TRANSPORT</a>. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ChangerQueryVolumeTags</b>

<dd>
<p>Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559417">IOCTL_CHANGER_QUERY_VOLUME_TAGS</a>. This routine has the following prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );</pre>
</td>
</tr>
</table></span></div>
</dd>
</dl>

## -remarks
<p>This structure is used by the changer driver in Windows XP and later operating systems only. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mcd.h (include Mcd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551400">ChangerAdditionalExtensionSize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551431">ChangerInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551418">ChangerError</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551438">ChangerPerformDiagnostics</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551425">ChangerGetParameters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551429">ChangerGetStatus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551427">ChangerGetProductData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551447">ChangerSetAccess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551424">ChangerGetElementStatus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551433">ChangerInitializeElementStatus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551449">ChangerSetPosition</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551421">ChangerExchangeMedium</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551436">ChangerMoveMedium</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551443">ChangerReinitializeUnit</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551440">ChangerQueryVolumeTags</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559399">IOCTL_CHANGER_GET_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559405">IOCTL_CHANGER_GET_STATUS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559402">IOCTL_CHANGER_GET_PRODUCT_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559422">IOCTL_CHANGER_SET_ACCESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559396">IOCTL_CHANGER_GET_ELEMENT_STATUS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559409">IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559425">IOCTL_CHANGER_SET_POSITION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559391">IOCTL_CHANGER_EXCHANGE_MEDIUM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559410">IOCTL_CHANGER_MOVE_MEDIUM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MCD_INIT_DATA structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
