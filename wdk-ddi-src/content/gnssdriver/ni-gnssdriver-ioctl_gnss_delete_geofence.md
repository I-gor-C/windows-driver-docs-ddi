---
UID: NI:gnssdriver.IOCTL_GNSS_DELETE_GEOFENCE
title: IOCTL_GNSS_DELETE_GEOFENCE
author: windows-driver-content
description: The IOCTL_GNSS_DELETE_GEOFENCE control code is used by the GNSS adapter to delete a previously created geofence.
old-location: sensors\ioctl_gnss_delete_geofence.htm
old-project: sensors
ms.assetid: BF50E28A-56CF-4718-93BB-CCC3DFE84072
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: IOCTL_GNSS_DELETE_GEOFENCE, IOCTL_GNSS_DELETE_GEOFENCE control code [Sensor Devices], gnssdriver/IOCTL_GNSS_DELETE_GEOFENCE, sensors.ioctl_gnss_delete_geofence
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	gnssdriver.h
api_name:
-	IOCTL_GNSS_DELETE_GEOFENCE
product:
- Windows
targetos: Windows
req.typenames: GNSS_SUPL_CERT_ACTION
---

# IOCTL_GNSS_DELETE_GEOFENCE IOCTL
The <b>IOCTL_GNSS_DELETE_GEOFENCE</b> control code is used by the GNSS adapter to delete a previously created geofence.


<div class="alert"><b>Note</b>  Applies to GNSS DDI version 2 and later.

</div><div> </div>

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn925168">GNSS_GEOFENCE_DELETE_PARAM</a> structure that defines the geofence to be deleted.

### Input Buffer Length
Set to sizeof(GNSS_GEOFENCE_DELETE_PARAM).

### Output Buffer
Set to <b>NULL</b>.

### Output Buffer Length
Set to 0.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.

## Remarks
NTSTATUS  with the following indications:

<ul>
<li>
STATUS_SUCCESS: The driver successfully removed the geofence.

</li>
<li>
STATUS_UNSUCCESSFUL: Failed, the geofence cannot be deleted.

</li>
</ul>
<h3><a id="GNSS_adapter_notes"></a><a id="gnss_adapter_notes"></a><a id="GNSS_ADAPTER_NOTES"></a>GNSS adapter notes</h3>
The GNSS adapter does not expect this call to fail because there is no elegant way to handle the consequence of this failure. On failure, the GNSS adapter will issue the <b>GNSS_ResetGeofencesTracking</b> command and re-add the geofences.

<h3><a id="GNSS_driver__notes"></a><a id="gnss_driver__notes"></a><a id="GNSS_DRIVER__NOTES"></a>GNSS driver  notes</h3>
If this is the last geofence, the GNSS driver should stop geofence tracking. If the GNSS engine was unable to track geofences (due to bad signal conditions or other transient errors) prior to the deletion of the last geofence, the monitoring activity should stop.

If the geofence is successfully removed, the driver returns STATUS_SUCCESS. If the geofence cannot be deleted, a failure code,  STATUS_UNSUCCESSFUL, is returned. If a failure occurs, the GNSS adapter issues the GNSS_ResetGeofencesTracking command and recreates the desired geofences. If this command deletes the last defined geofence, the driver stops geofence tracking.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | gnssdriver.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548651">WdfIoTargetSendInternalIoctlOthersSynchronously</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548656">WdfIoTargetSendInternalIoctlSynchronously</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548660">WdfIoTargetSendIoctlSynchronously</a>