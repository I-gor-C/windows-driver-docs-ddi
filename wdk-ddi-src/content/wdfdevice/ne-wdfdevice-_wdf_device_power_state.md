---
UID: NE:wdfdevice._WDF_DEVICE_POWER_STATE
title: "_WDF_DEVICE_POWER_STATE"
author: windows-driver-content
description: The WDF_DEVICE_POWER_STATE enumeration identifies all of the states that the framework's power state machine can enter.
old-location: wdf\wdf_device_power_state.htm
old-project: wdf
ms.assetid: 06bb6465-afc6-4b92-b3d7-1c66f6c6c33d
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PWDF_DEVICE_POWER_STATE, DFDeviceObjectGeneralRef_f8548618-261b-4461-adfa-eeee324e67c2.xml, PWDF_DEVICE_POWER_STATE, PWDF_DEVICE_POWER_STATE enumeration pointer, WDF_DEVICE_POWER_STATE, WDF_DEVICE_POWER_STATE enumeration, WdfDevStatePowerCheckDeviceType, WdfDevStatePowerCheckDeviceTypeNP, WdfDevStatePowerCheckParentState, WdfDevStatePowerCheckParentStateArmedForWake, WdfDevStatePowerCheckParentStateArmedForWakeNP, WdfDevStatePowerCheckParentStateNP, WdfDevStatePowerD0, WdfDevStatePowerD0ArmedForWake, WdfDevStatePowerD0ArmedForWakeNP, WdfDevStatePowerD0BusWakeOwner, WdfDevStatePowerD0BusWakeOwnerNP, WdfDevStatePowerD0DisarmingWakeAtBus, WdfDevStatePowerD0DisarmingWakeAtBusNP, WdfDevStatePowerD0NP, WdfDevStatePowerD0Starting, WdfDevStatePowerD0StartingConnectInterrupt, WdfDevStatePowerD0StartingDmaEnable, WdfDevStatePowerD0StartingStartSelfManagedIo, WdfDevStatePowerDecideD0State, WdfDevStatePowerDx, WdfDevStatePowerDxArmedForWake, WdfDevStatePowerDxArmedForWakeNP, WdfDevStatePowerDxDisablingWakeAtBus, WdfDevStatePowerDxDisablingWakeAtBusNP, WdfDevStatePowerDxNP, WdfDevStatePowerDxStopped, WdfDevStatePowerDxStoppedArmForWake, WdfDevStatePowerDxStoppedArmForWakeNP, WdfDevStatePowerDxStoppedDecideDxState, WdfDevStatePowerDxStoppedDisarmWake, WdfDevStatePowerDxStoppedDisarmWakeNP, WdfDevStatePowerEnablingWakeAtBus, WdfDevStatePowerEnablingWakeAtBusNP, WdfDevStatePowerFinal, WdfDevStatePowerFinalPowerDownFailed, WdfDevStatePowerGotoD3Stopped, WdfDevStatePowerGotoDx, WdfDevStatePowerGotoDxArmedForWake, WdfDevStatePowerGotoDxArmedForWakeNP, WdfDevStatePowerGotoDxFailed, WdfDevStatePowerGotoDxIoStopped, WdfDevStatePowerGotoDxIoStoppedArmedForWake, WdfDevStatePowerGotoDxIoStoppedArmedForWakeNP, WdfDevStatePowerGotoDxIoStoppedNP, WdfDevStatePowerGotoDxNP, WdfDevStatePowerGotoDxNPFailed, WdfDevStatePowerGotoDxStopped, WdfDevStatePowerGotoDxStoppedDisableInterrupt, WdfDevStatePowerGotoDxStoppedDisableInterruptNP, WdfDevStatePowerGotoImplicitD3DisarmWakeAtBus, WdfDevStatePowerGotoStopped, WdfDevStatePowerInitialConnectInterruptFailed, WdfDevStatePowerInitialDmaEnableFailed, WdfDevStatePowerInitialPowerUpFailed, WdfDevStatePowerInitialPowerUpFailedDerefParent, WdfDevStatePowerInitialPowerUpFailedPowerDown, WdfDevStatePowerInitialSelfManagedIoFailed, WdfDevStatePowerInitialSelfManagedIoFailedStarted, WdfDevStatePowerInvalid, WdfDevStatePowerNotifyingD0EntryToWakeInterrupts, WdfDevStatePowerNotifyingD0EntryToWakeInterruptsNP, WdfDevStatePowerNotifyingD0ExitToWakeInterrupts, WdfDevStatePowerNotifyingD0ExitToWakeInterruptsNP, WdfDevStatePowerNull, WdfDevStatePowerObjectCreated, WdfDevStatePowerPowerFailedPowerDown, WdfDevStatePowerReportPowerDownFailed, WdfDevStatePowerReportPowerUpFailed, WdfDevStatePowerReportPowerUpFailedDerefParent, WdfDevStatePowerStartSelfManagedIo, WdfDevStatePowerStartSelfManagedIoFailed, WdfDevStatePowerStartSelfManagedIoFailedNP, WdfDevStatePowerStartSelfManagedIoFailedStarted, WdfDevStatePowerStartSelfManagedIoFailedStartedNP, WdfDevStatePowerStartSelfManagedIoNP, WdfDevStatePowerStartingCheckDeviceType, WdfDevStatePowerStartingChild, WdfDevStatePowerStopped, WdfDevStatePowerStoppedCompleteDx, WdfDevStatePowerUpFailed, WdfDevStatePowerUpFailedDerefParent, WdfDevStatePowerUpFailedDerefParentNP, WdfDevStatePowerUpFailedNP, WdfDevStatePowerUpFailedPowerDown, WdfDevStatePowerUpFailedPowerDownNP, WdfDevStatePowerWaitForParent, WdfDevStatePowerWaitForParentArmedForWake, WdfDevStatePowerWaitForParentArmedForWakeNP, WdfDevStatePowerWaitForParentNP, WdfDevStatePowerWakePending, WdfDevStatePowerWakePendingNP, WdfDevStatePowerWaking, WdfDevStatePowerWakingConnectInterrupt, WdfDevStatePowerWakingConnectInterruptFailed, WdfDevStatePowerWakingConnectInterruptFailedNP, WdfDevStatePowerWakingConnectInterruptNP, WdfDevStatePowerWakingDmaEnable, WdfDevStatePowerWakingDmaEnableFailed, WdfDevStatePowerWakingDmaEnableFailedNP, WdfDevStatePowerWakingDmaEnableNP, WdfDevStatePowerWakingNP, _WDF_DEVICE_POWER_STATE, kmdf.wdf_device_power_state, wdf.wdf_device_power_state, wdfdevice/PWDF_DEVICE_POWER_STATE, wdfdevice/WDF_DEVICE_POWER_STATE, wdfdevice/WdfDevStatePowerCheckDeviceType, wdfdevice/WdfDevStatePowerCheckDeviceTypeNP, wdfdevice/WdfDevStatePowerCheckParentState, wdfdevice/WdfDevStatePowerCheckParentStateArmedForWake, wdfdevice/WdfDevStatePowerCheckParentStateArmedForWakeNP, wdfdevice/WdfDevStatePowerCheckParentStateNP, wdfdevice/WdfDevStatePowerD0, wdfdevice/WdfDevStatePowerD0ArmedForWake, wdfdevice/WdfDevStatePowerD0ArmedForWakeNP, wdfdevice/WdfDevStatePowerD0BusWakeOwner, wdfdevice/WdfDevStatePowerD0BusWakeOwnerNP, wdfdevice/WdfDevStatePowerD0DisarmingWakeAtBus, wdfdevice/WdfDevStatePowerD0DisarmingWakeAtBusNP, wdfdevice/WdfDevStatePowerD0NP, wdfdevice/WdfDevStatePowerD0Starting, wdfdevice/WdfDevStatePowerD0StartingConnectInterrupt, wdfdevice/WdfDevStatePowerD0StartingDmaEnable, wdfdevice/WdfDevStatePowerD0StartingStartSelfManagedIo, wdfdevice/WdfDevStatePowerDecideD0State, wdfdevice/WdfDevStatePowerDx, wdfdevice/WdfDevStatePowerDxArmedForWake, wdfdevice/WdfDevStatePowerDxArmedForWakeNP, wdfdevice/WdfDevStatePowerDxDisablingWakeAtBus, wdfdevice/WdfDevStatePowerDxDisablingWakeAtBusNP, wdfdevice/WdfDevStatePowerDxNP, wdfdevice/WdfDevStatePowerDxStopped, wdfdevice/WdfDevStatePowerDxStoppedArmForWake, wdfdevice/WdfDevStatePowerDxStoppedArmForWakeNP, wdfdevice/WdfDevStatePowerDxStoppedDecideDxState, wdfdevice/WdfDevStatePowerDxStoppedDisarmWake, wdfdevice/WdfDevStatePowerDxStoppedDisarmWakeNP, wdfdevice/WdfDevStatePowerEnablingWakeAtBus, wdfdevice/WdfDevStatePowerEnablingWakeAtBusNP, wdfdevice/WdfDevStatePowerFinal, wdfdevice/WdfDevStatePowerFinalPowerDownFailed, wdfdevice/WdfDevStatePowerGotoD3Stopped, wdfdevice/WdfDevStatePowerGotoDx, wdfdevice/WdfDevStatePowerGotoDxArmedForWake, wdfdevice/WdfDevStatePowerGotoDxArmedForWakeNP, wdfdevice/WdfDevStatePowerGotoDxFailed, wdfdevice/WdfDevStatePowerGotoDxIoStopped, wdfdevice/WdfDevStatePowerGotoDxIoStoppedArmedForWake, wdfdevice/WdfDevStatePowerGotoDxIoStoppedArmedForWakeNP, wdfdevice/WdfDevStatePowerGotoDxIoStoppedNP, wdfdevice/WdfDevStatePowerGotoDxNP, wdfdevice/WdfDevStatePowerGotoDxNPFailed, wdfdevice/WdfDevStatePowerGotoDxStopped, wdfdevice/WdfDevStatePowerGotoDxStoppedDisableInterrupt, wdfdevice/WdfDevStatePowerGotoDxStoppedDisableInterruptNP, wdfdevice/WdfDevStatePowerGotoImplicitD3DisarmWakeAtBus, wdfdevice/WdfDevStatePowerGotoStopped, wdfdevice/WdfDevStatePowerInitialConnectInterruptFailed, wdfdevice/WdfDevStatePowerInitialDmaEnableFailed, wdfdevice/WdfDevStatePowerInitialPowerUpFailed, wdfdevice/WdfDevStatePowerInitialPowerUpFailedDerefParent, wdfdevice/WdfDevStatePowerInitialPowerUpFailedPowerDown, wdfdevice/WdfDevStatePowerInitialSelfManagedIoFailed, wdfdevice/WdfDevStatePowerInitialSelfManagedIoFailedStarted, wdfdevice/WdfDevStatePowerInvalid, wdfdevice/WdfDevStatePowerNotifyingD0EntryToWakeInterrupts, wdfdevice/WdfDevStatePowerNotifyingD0EntryToWakeInterruptsNP, wdfdevice/WdfDevStatePowerNotifyingD0ExitToWakeInterrupts, wdfdevice/WdfDevStatePowerNotifyingD0ExitToWakeInterruptsNP, wdfdevice/WdfDevStatePowerNull, wdfdevice/WdfDevStatePowerObjectCreated, wdfdevice/WdfDevStatePowerPowerFailedPowerDown, wdfdevice/WdfDevStatePowerReportPowerDownFailed, wdfdevice/WdfDevStatePowerReportPowerUpFailed, wdfdevice/WdfDevStatePowerReportPowerUpFailedDerefParent, wdfdevice/WdfDevStatePowerStartSelfManagedIo, wdfdevice/WdfDevStatePowerStartSelfManagedIoFailed, wdfdevice/WdfDevStatePowerStartSelfManagedIoFailedNP, wdfdevice/WdfDevStatePowerStartSelfManagedIoFailedStarted, wdfdevice/WdfDevStatePowerStartSelfManagedIoFailedStartedNP, wdfdevice/WdfDevStatePowerStartSelfManagedIoNP, wdfdevice/WdfDevStatePowerStartingCheckDeviceType, wdfdevice/WdfDevStatePowerStartingChild, wdfdevice/WdfDevStatePowerStopped, wdfdevice/WdfDevStatePowerStoppedCompleteDx, wdfdevice/WdfDevStatePowerUpFailed, wdfdevice/WdfDevStatePowerUpFailedDerefParent, wdfdevice/WdfDevStatePowerUpFailedDerefParentNP, wdfdevice/WdfDevStatePowerUpFailedNP, wdfdevice/WdfDevStatePowerUpFailedPowerDown, wdfdevice/WdfDevStatePowerUpFailedPowerDownNP, wdfdevice/WdfDevStatePowerWaitForParent, wdfdevice/WdfDevStatePowerWaitForParentArmedForWake, wdfdevice/WdfDevStatePowerWaitForParentArmedForWakeNP, wdfdevice/WdfDevStatePowerWaitForParentNP, wdfdevice/WdfDevStatePowerWakePending, wdfdevice/WdfDevStatePowerWakePendingNP, wdfdevice/WdfDevStatePowerWaking, wdfdevice/WdfDevStatePowerWakingConnectInterrupt, wdfdevice/WdfDevStatePowerWakingConnectInterruptFailed, wdfdevice/WdfDevStatePowerWakingConnectInterruptFailedNP, wdfdevice/WdfDevStatePowerWakingConnectInterruptNP, wdfdevice/WdfDevStatePowerWakingDmaEnable, wdfdevice/WdfDevStatePowerWakingDmaEnableFailed, wdfdevice/WdfDevStatePowerWakingDmaEnableFailedNP, wdfdevice/WdfDevStatePowerWakingDmaEnableNP, wdfdevice/WdfDevStatePowerWakingNP"
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
-	WDF_DEVICE_POWER_STATE
product:
- Windows
targetos: Windows
req.typenames: WDF_DEVICE_POWER_STATE, *PWDF_DEVICE_POWER_STATE
req.product: Windows 10 or later.
---

# _WDF_DEVICE_POWER_STATE Enumeration
<p class="CCE_Message">[Applies to KMDF only]

The <b>WDF_DEVICE_POWER_STATE</b> enumeration identifies all of the states that the framework's power state machine can enter.

## Syntax
```
typedef enum _WDF_DEVICE_POWER_STATE {
  WdfDevStatePowerInvalid                             ,
  WdfDevStatePowerObjectCreated                       ,
  WdfDevStatePowerCheckDeviceType                     ,
  WdfDevStatePowerCheckDeviceTypeNP                   ,
  WdfDevStatePowerCheckParentState                    ,
  WdfDevStatePowerCheckParentStateNP                  ,
  WdfDevStatePowerEnablingWakeAtBus                   ,
  WdfDevStatePowerEnablingWakeAtBusNP                 ,
  WdfDevStatePowerD0                                  ,
  WdfDevStatePowerD0NP                                ,
  WdfDevStatePowerD0BusWakeOwner                      ,
  WdfDevStatePowerD0BusWakeOwnerNP                    ,
  WdfDevStatePowerD0ArmedForWake                      ,
  WdfDevStatePowerD0ArmedForWakeNP                    ,
  WdfDevStatePowerD0DisarmingWakeAtBus                ,
  WdfDevStatePowerD0DisarmingWakeAtBusNP              ,
  WdfDevStatePowerD0Starting                          ,
  WdfDevStatePowerD0StartingConnectInterrupt          ,
  WdfDevStatePowerD0StartingDmaEnable                 ,
  WdfDevStatePowerD0StartingStartSelfManagedIo        ,
  WdfDevStatePowerDecideD0State                       ,
  WdfDevStatePowerGotoD3Stopped                       ,
  WdfDevStatePowerStopped                             ,
  WdfDevStatePowerStartingCheckDeviceType             ,
  WdfDevStatePowerStartingChild                       ,
  WdfDevStatePowerDxDisablingWakeAtBus                ,
  WdfDevStatePowerDxDisablingWakeAtBusNP              ,
  WdfDevStatePowerGotoDx                              ,
  WdfDevStatePowerGotoDxNP                            ,
  WdfDevStatePowerGotoDxIoStopped                     ,
  WdfDevStatePowerGotoDxIoStoppedNP                   ,
  WdfDevStatePowerGotoDxNPFailed                      ,
  WdfDevStatePowerDx                                  ,
  WdfDevStatePowerDxNP                                ,
  WdfDevStatePowerGotoDxArmedForWake                  ,
  WdfDevStatePowerGotoDxArmedForWakeNP                ,
  WdfDevStatePowerGotoDxIoStoppedArmedForWake         ,
  WdfDevStatePowerGotoDxIoStoppedArmedForWakeNP       ,
  WdfDevStatePowerDxArmedForWake                      ,
  WdfDevStatePowerDxArmedForWakeNP                    ,
  WdfDevStatePowerCheckParentStateArmedForWake        ,
  WdfDevStatePowerCheckParentStateArmedForWakeNP      ,
  WdfDevStatePowerWaitForParentArmedForWake           ,
  WdfDevStatePowerWaitForParentArmedForWakeNP         ,
  WdfDevStatePowerStartSelfManagedIo                  ,
  WdfDevStatePowerStartSelfManagedIoNP                ,
  WdfDevStatePowerStartSelfManagedIoFailed            ,
  WdfDevStatePowerStartSelfManagedIoFailedNP          ,
  WdfDevStatePowerWaitForParent                       ,
  WdfDevStatePowerWaitForParentNP                     ,
  WdfDevStatePowerWakePending                         ,
  WdfDevStatePowerWakePendingNP                       ,
  WdfDevStatePowerWaking                              ,
  WdfDevStatePowerWakingNP                            ,
  WdfDevStatePowerWakingConnectInterrupt              ,
  WdfDevStatePowerWakingConnectInterruptNP            ,
  WdfDevStatePowerWakingConnectInterruptFailed        ,
  WdfDevStatePowerWakingConnectInterruptFailedNP      ,
  WdfDevStatePowerWakingDmaEnable                     ,
  WdfDevStatePowerWakingDmaEnableNP                   ,
  WdfDevStatePowerWakingDmaEnableFailed               ,
  WdfDevStatePowerWakingDmaEnableFailedNP             ,
  WdfDevStatePowerReportPowerUpFailedDerefParent      ,
  WdfDevStatePowerReportPowerUpFailed                 ,
  WdfDevStatePowerPowerFailedPowerDown                ,
  WdfDevStatePowerReportPowerDownFailed               ,
  WdfDevStatePowerInitialConnectInterruptFailed       ,
  WdfDevStatePowerInitialDmaEnableFailed              ,
  WdfDevStatePowerInitialSelfManagedIoFailed          ,
  WdfDevStatePowerInitialPowerUpFailedDerefParent     ,
  WdfDevStatePowerInitialPowerUpFailed                ,
  WdfDevStatePowerDxStoppedDisarmWake                 ,
  WdfDevStatePowerDxStoppedDisarmWakeNP               ,
  WdfDevStatePowerGotoDxStoppedDisableInterruptNP     ,
  WdfDevStatePowerGotoDxStopped                       ,
  WdfDevStatePowerDxStopped                           ,
  WdfDevStatePowerGotoStopped                         ,
  WdfDevStatePowerStoppedCompleteDx                   ,
  WdfDevStatePowerDxStoppedDecideDxState              ,
  WdfDevStatePowerDxStoppedArmForWake                 ,
  WdfDevStatePowerDxStoppedArmForWakeNP               ,
  WdfDevStatePowerFinalPowerDownFailed                ,
  WdfDevStatePowerFinal                               ,
  WdfDevStatePowerGotoImplicitD3DisarmWakeAtBus       ,
  WdfDevStatePowerUpFailed                            ,
  WdfDevStatePowerUpFailedDerefParent                 ,
  WdfDevStatePowerGotoDxFailed                        ,
  WdfDevStatePowerGotoDxStoppedDisableInterrupt       ,
  WdfDevStatePowerUpFailedNP                          ,
  WdfDevStatePowerUpFailedDerefParentNP               ,
  WdfDevStatePowerNotifyingD0ExitToWakeInterrupts     ,
  WdfDevStatePowerNotifyingD0EntryToWakeInterrupts    ,
  WdfDevStatePowerNotifyingD0ExitToWakeInterruptsNP   ,
  WdfDevStatePowerNotifyingD0EntryToWakeInterruptsNP  ,
  WdfDevStatePowerInitialPowerUpFailedPowerDown       ,
  WdfDevStatePowerUpFailedPowerDown                   ,
  WdfDevStatePowerUpFailedPowerDownNP                 ,
  WdfDevStatePowerInitialSelfManagedIoFailedStarted   ,
  WdfDevStatePowerStartSelfManagedIoFailedStarted     ,
  WdfDevStatePowerStartSelfManagedIoFailedStartedNP   ,
  WdfDevStatePowerNull
} WDF_DEVICE_POWER_STATE, *PWDF_DEVICE_POWER_STATE;
```

## Constants

<table>
            
                <tr>
                    <td>WdfDevStatePowerInvalid</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerObjectCreated</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerCheckDeviceType</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerCheckDeviceTypeNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerCheckParentState</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerCheckParentStateNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerEnablingWakeAtBus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerEnablingWakeAtBusNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0NP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0BusWakeOwner</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0BusWakeOwnerNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0ArmedForWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0ArmedForWakeNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0DisarmingWakeAtBus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0DisarmingWakeAtBusNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0Starting</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0StartingConnectInterrupt</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0StartingDmaEnable</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0StartingStartSelfManagedIo</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDecideD0State</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoD3Stopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStartingCheckDeviceType</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStartingChild</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxDisablingWakeAtBus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxDisablingWakeAtBusNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDx</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxIoStopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxIoStoppedNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxNPFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDx</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxArmedForWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxArmedForWakeNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxIoStoppedArmedForWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxIoStoppedArmedForWakeNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxArmedForWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxArmedForWakeNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerCheckParentStateArmedForWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerCheckParentStateArmedForWakeNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWaitForParentArmedForWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWaitForParentArmedForWakeNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStartSelfManagedIo</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStartSelfManagedIoNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStartSelfManagedIoFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStartSelfManagedIoFailedNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWaitForParent</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWaitForParentNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakePending</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakePendingNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWaking</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakingNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakingConnectInterrupt</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakingConnectInterruptNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakingConnectInterruptFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakingConnectInterruptFailedNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakingDmaEnable</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakingDmaEnableNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakingDmaEnableFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakingDmaEnableFailedNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerReportPowerUpFailedDerefParent</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerReportPowerUpFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerPowerFailedPowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerReportPowerDownFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInitialConnectInterruptFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInitialDmaEnableFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInitialSelfManagedIoFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInitialPowerUpFailedDerefParent</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInitialPowerUpFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxStoppedDisarmWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxStoppedDisarmWakeNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxStoppedDisableInterruptNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxStopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxStopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoStopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStoppedCompleteDx</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxStoppedDecideDxState</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxStoppedArmForWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxStoppedArmForWakeNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerFinalPowerDownFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerFinal</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoImplicitD3DisarmWakeAtBus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerUpFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerUpFailedDerefParent</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxStoppedDisableInterrupt</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerUpFailedNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerUpFailedDerefParentNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerNotifyingD0ExitToWakeInterrupts</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerNotifyingD0EntryToWakeInterrupts</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerNotifyingD0ExitToWakeInterruptsNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerNotifyingD0EntryToWakeInterruptsNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInitialPowerUpFailedPowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerUpFailedPowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerUpFailedPowerDownNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInitialSelfManagedIoFailedStarted</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStartSelfManagedIoFailedStarted</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStartSelfManagedIoFailedStartedNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerNull</td>
                    <td></td>
                </tr>
</table>

## Remarks

The <b>WDF_DEVICE_POWER_STATE</b> enumeration is used as a member type in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551268">WDF_DEVICE_POWER_NOTIFICATION_DATA</a> structure and as the return type for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545985">WdfDeviceGetDevicePowerState</a> method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Header** | wdfdevice.h (include Wdf.h) |