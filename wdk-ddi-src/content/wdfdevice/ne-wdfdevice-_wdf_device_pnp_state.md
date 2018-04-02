---
UID: NE:wdfdevice._WDF_DEVICE_PNP_STATE
title: "_WDF_DEVICE_PNP_STATE"
author: windows-driver-content
description: The WDF_DEVICE_PNP_STATE enumeration identifies all of the states that the framework's Plug and Play state machine can enter.
old-location: wdf\wdf_device_pnp_state.htm
old-project: wdf
ms.assetid: b907a1ca-d9ef-45e9-9e1b-26e58e3e1e07
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PWDF_DEVICE_PNP_STATE, DFDeviceObjectGeneralRef_e9aab8ea-3d0c-44f3-bad9-cd21c6f1bd28.xml, PWDF_DEVICE_PNP_STATE, PWDF_DEVICE_PNP_STATE enumeration pointer, WDF_DEVICE_PNP_STATE, WDF_DEVICE_PNP_STATE enumeration, WdfDevStatePnpCheckForDevicePresence, WdfDevStatePnpEjectFailed, WdfDevStatePnpEjectHardware, WdfDevStatePnpEjectedWaitingForRemove, WdfDevStatePnpEnableInterfaces, WdfDevStatePnpFailed, WdfDevStatePnpFailedInit, WdfDevStatePnpFailedIoStarting, WdfDevStatePnpFailedOwnHardware, WdfDevStatePnpFailedPowerDown, WdfDevStatePnpFailedPowerPolicyRemoved, WdfDevStatePnpFailedStarted, WdfDevStatePnpFailedSurpriseRemoved, WdfDevStatePnpFailedWaitForRemove, WdfDevStatePnpFdoRemoved, WdfDevStatePnpFinal, WdfDevStatePnpHardwareAvailable, WdfDevStatePnpHardwareAvailablePowerPolicyFailed, WdfDevStatePnpInit, WdfDevStatePnpInitQueryRemove, WdfDevStatePnpInitQueryRemoveCanceled, WdfDevStatePnpInitStarting, WdfDevStatePnpInitSurpriseRemoved, WdfDevStatePnpInvalid, WdfDevStatePnpNull, WdfDevStatePnpObjectCreated, WdfDevStatePnpPdoInitFailed, WdfDevStatePnpPdoRemoved, WdfDevStatePnpPdoRestart, WdfDevStatePnpQueriedRemoving, WdfDevStatePnpQueriedSurpriseRemove, WdfDevStatePnpQueryCanceled, WdfDevStatePnpQueryRemoveAskDriver, WdfDevStatePnpQueryRemoveEnsureDeviceAwake, WdfDevStatePnpQueryRemovePending, WdfDevStatePnpQueryRemoveStaticCheck, WdfDevStatePnpQueryStopAskDriver, WdfDevStatePnpQueryStopEnsureDeviceAwake, WdfDevStatePnpQueryStopPending, WdfDevStatePnpQueryStopStaticCheck, WdfDevStatePnpRemoved, WdfDevStatePnpRemovedChildrenRemoved, WdfDevStatePnpRemovedPdoSurpriseRemoved, WdfDevStatePnpRemovedPdoWait, WdfDevStatePnpRemovedWaitForChildren, WdfDevStatePnpRemovingDisableInterfaces, WdfDevStatePnpRestart, WdfDevStatePnpRestartHardwareAvailable, WdfDevStatePnpRestartReleaseHardware, WdfDevStatePnpRestarting, WdfDevStatePnpStarted, WdfDevStatePnpStartedCancelRemove, WdfDevStatePnpStartedCancelStop, WdfDevStatePnpStartedRemoving, WdfDevStatePnpStartedStopping, WdfDevStatePnpStartingFromStopped, WdfDevStatePnpStopped, WdfDevStatePnpStoppedWaitForStartCompletion, WdfDevStatePnpSurpriseRemove, WdfDevStatePnpSurpriseRemoveIoStarted, _WDF_DEVICE_PNP_STATE, kmdf.wdf_device_pnp_state, wdf.wdf_device_pnp_state, wdfdevice/PWDF_DEVICE_PNP_STATE, wdfdevice/WDF_DEVICE_PNP_STATE, wdfdevice/WdfDevStatePnpCheckForDevicePresence, wdfdevice/WdfDevStatePnpEjectFailed, wdfdevice/WdfDevStatePnpEjectHardware, wdfdevice/WdfDevStatePnpEjectedWaitingForRemove, wdfdevice/WdfDevStatePnpEnableInterfaces, wdfdevice/WdfDevStatePnpFailed, wdfdevice/WdfDevStatePnpFailedInit, wdfdevice/WdfDevStatePnpFailedIoStarting, wdfdevice/WdfDevStatePnpFailedOwnHardware, wdfdevice/WdfDevStatePnpFailedPowerDown, wdfdevice/WdfDevStatePnpFailedPowerPolicyRemoved, wdfdevice/WdfDevStatePnpFailedStarted, wdfdevice/WdfDevStatePnpFailedSurpriseRemoved, wdfdevice/WdfDevStatePnpFailedWaitForRemove, wdfdevice/WdfDevStatePnpFdoRemoved, wdfdevice/WdfDevStatePnpFinal, wdfdevice/WdfDevStatePnpHardwareAvailable, wdfdevice/WdfDevStatePnpHardwareAvailablePowerPolicyFailed, wdfdevice/WdfDevStatePnpInit, wdfdevice/WdfDevStatePnpInitQueryRemove, wdfdevice/WdfDevStatePnpInitQueryRemoveCanceled, wdfdevice/WdfDevStatePnpInitStarting, wdfdevice/WdfDevStatePnpInitSurpriseRemoved, wdfdevice/WdfDevStatePnpInvalid, wdfdevice/WdfDevStatePnpNull, wdfdevice/WdfDevStatePnpObjectCreated, wdfdevice/WdfDevStatePnpPdoInitFailed, wdfdevice/WdfDevStatePnpPdoRemoved, wdfdevice/WdfDevStatePnpPdoRestart, wdfdevice/WdfDevStatePnpQueriedRemoving, wdfdevice/WdfDevStatePnpQueriedSurpriseRemove, wdfdevice/WdfDevStatePnpQueryCanceled, wdfdevice/WdfDevStatePnpQueryRemoveAskDriver, wdfdevice/WdfDevStatePnpQueryRemoveEnsureDeviceAwake, wdfdevice/WdfDevStatePnpQueryRemovePending, wdfdevice/WdfDevStatePnpQueryRemoveStaticCheck, wdfdevice/WdfDevStatePnpQueryStopAskDriver, wdfdevice/WdfDevStatePnpQueryStopEnsureDeviceAwake, wdfdevice/WdfDevStatePnpQueryStopPending, wdfdevice/WdfDevStatePnpQueryStopStaticCheck, wdfdevice/WdfDevStatePnpRemoved, wdfdevice/WdfDevStatePnpRemovedChildrenRemoved, wdfdevice/WdfDevStatePnpRemovedPdoSurpriseRemoved, wdfdevice/WdfDevStatePnpRemovedPdoWait, wdfdevice/WdfDevStatePnpRemovedWaitForChildren, wdfdevice/WdfDevStatePnpRemovingDisableInterfaces, wdfdevice/WdfDevStatePnpRestart, wdfdevice/WdfDevStatePnpRestartHardwareAvailable, wdfdevice/WdfDevStatePnpRestartReleaseHardware, wdfdevice/WdfDevStatePnpRestarting, wdfdevice/WdfDevStatePnpStarted, wdfdevice/WdfDevStatePnpStartedCancelRemove, wdfdevice/WdfDevStatePnpStartedCancelStop, wdfdevice/WdfDevStatePnpStartedRemoving, wdfdevice/WdfDevStatePnpStartedStopping, wdfdevice/WdfDevStatePnpStartingFromStopped, wdfdevice/WdfDevStatePnpStopped, wdfdevice/WdfDevStatePnpStoppedWaitForStartCompletion, wdfdevice/WdfDevStatePnpSurpriseRemove, wdfdevice/WdfDevStatePnpSurpriseRemoveIoStarted"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
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
req.irql: See Remarks section.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdfdevice.h
api_name:
-	WDF_DEVICE_PNP_STATE
product:
- Windows
targetos: Windows
req.typenames: WDF_DEVICE_PNP_STATE, *PWDF_DEVICE_PNP_STATE
req.product: Windows 10 or later.
---

# _WDF_DEVICE_PNP_STATE Enumeration
<p class="CCE_Message">[Applies to KMDF only]

The WDF_DEVICE_PNP_STATE enumeration identifies all of the states that the framework's Plug and Play state machine can enter.

## Syntax
```
typedef enum _WDF_DEVICE_PNP_STATE {
  WdfDevStatePnpInvalid                             ,
  WdfDevStatePnpObjectCreated                       ,
  WdfDevStatePnpCheckForDevicePresence              ,
  WdfDevStatePnpEjectFailed                         ,
  WdfDevStatePnpEjectHardware                       ,
  WdfDevStatePnpEjectedWaitingForRemove             ,
  WdfDevStatePnpInit                                ,
  WdfDevStatePnpInitStarting                        ,
  WdfDevStatePnpInitSurpriseRemoved                 ,
  WdfDevStatePnpHardwareAvailable                   ,
  WdfDevStatePnpEnableInterfaces                    ,
  WdfDevStatePnpHardwareAvailablePowerPolicyFailed  ,
  WdfDevStatePnpQueryRemoveAskDriver                ,
  WdfDevStatePnpQueryRemovePending                  ,
  WdfDevStatePnpQueryRemoveStaticCheck              ,
  WdfDevStatePnpQueriedRemoving                     ,
  WdfDevStatePnpQueryStopAskDriver                  ,
  WdfDevStatePnpQueryStopPending                    ,
  WdfDevStatePnpQueryStopStaticCheck                ,
  WdfDevStatePnpQueryCanceled                       ,
  WdfDevStatePnpRemoved                             ,
  WdfDevStatePnpPdoRemoved                          ,
  WdfDevStatePnpRemovedPdoWait                      ,
  WdfDevStatePnpRemovedPdoSurpriseRemoved           ,
  WdfDevStatePnpRemovingDisableInterfaces           ,
  WdfDevStatePnpRestarting                          ,
  WdfDevStatePnpStarted                             ,
  WdfDevStatePnpStartedCancelStop                   ,
  WdfDevStatePnpStartedCancelRemove                 ,
  WdfDevStatePnpStartedRemoving                     ,
  WdfDevStatePnpStartingFromStopped                 ,
  WdfDevStatePnpStopped                             ,
  WdfDevStatePnpStoppedWaitForStartCompletion       ,
  WdfDevStatePnpStartedStopping                     ,
  WdfDevStatePnpSurpriseRemove                      ,
  WdfDevStatePnpInitQueryRemove                     ,
  WdfDevStatePnpInitQueryRemoveCanceled             ,
  WdfDevStatePnpFdoRemoved                          ,
  WdfDevStatePnpRemovedWaitForChildren              ,
  WdfDevStatePnpQueriedSurpriseRemove               ,
  WdfDevStatePnpSurpriseRemoveIoStarted             ,
  WdfDevStatePnpFailedPowerDown                     ,
  WdfDevStatePnpFailedIoStarting                    ,
  WdfDevStatePnpFailedOwnHardware                   ,
  WdfDevStatePnpFailed                              ,
  WdfDevStatePnpFailedSurpriseRemoved               ,
  WdfDevStatePnpFailedStarted                       ,
  WdfDevStatePnpFailedWaitForRemove                 ,
  WdfDevStatePnpFailedInit                          ,
  WdfDevStatePnpPdoInitFailed                       ,
  WdfDevStatePnpRestart                             ,
  WdfDevStatePnpRestartReleaseHardware              ,
  WdfDevStatePnpRestartHardwareAvailable            ,
  WdfDevStatePnpPdoRestart                          ,
  WdfDevStatePnpFinal                               ,
  WdfDevStatePnpRemovedChildrenRemoved              ,
  WdfDevStatePnpQueryRemoveEnsureDeviceAwake        ,
  WdfDevStatePnpQueryStopEnsureDeviceAwake          ,
  WdfDevStatePnpFailedPowerPolicyRemoved            ,
  WdfDevStatePnpNull
} WDF_DEVICE_PNP_STATE, *PWDF_DEVICE_PNP_STATE;
```

## Constants

<table>
            
                <tr>
                    <td>WdfDevStatePnpInvalid</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpObjectCreated</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpCheckForDevicePresence</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpEjectFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpEjectHardware</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpEjectedWaitingForRemove</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpInit</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpInitStarting</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpInitSurpriseRemoved</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpHardwareAvailable</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpEnableInterfaces</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpHardwareAvailablePowerPolicyFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpQueryRemoveAskDriver</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpQueryRemovePending</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpQueryRemoveStaticCheck</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpQueriedRemoving</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpQueryStopAskDriver</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpQueryStopPending</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpQueryStopStaticCheck</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpQueryCanceled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpRemoved</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpPdoRemoved</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpRemovedPdoWait</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpRemovedPdoSurpriseRemoved</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpRemovingDisableInterfaces</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpRestarting</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpStarted</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpStartedCancelStop</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpStartedCancelRemove</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpStartedRemoving</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpStartingFromStopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpStopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpStoppedWaitForStartCompletion</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpStartedStopping</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpSurpriseRemove</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpInitQueryRemove</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpInitQueryRemoveCanceled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpFdoRemoved</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpRemovedWaitForChildren</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpQueriedSurpriseRemove</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpSurpriseRemoveIoStarted</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpFailedPowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpFailedIoStarting</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpFailedOwnHardware</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpFailedSurpriseRemoved</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpFailedStarted</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpFailedWaitForRemove</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpFailedInit</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpPdoInitFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpRestart</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpRestartReleaseHardware</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpRestartHardwareAvailable</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpPdoRestart</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpFinal</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpRemovedChildrenRemoved</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpQueryRemoveEnsureDeviceAwake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpQueryStopEnsureDeviceAwake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpFailedPowerPolicyRemoved</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePnpNull</td>
                    <td></td>
                </tr>
</table>

## Remarks

The WDF_DEVICE_PNP_STATE enumeration is used as a member type for  the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551260">WDF_DEVICE_PNP_NOTIFICATION_DATA</a> structure and as the return type for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545969">WdfDeviceGetDevicePnpState</a> method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Header** | wdfdevice.h (include Wdf.h) |