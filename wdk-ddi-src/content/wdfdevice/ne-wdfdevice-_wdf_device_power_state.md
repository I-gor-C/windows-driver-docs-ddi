---
UID: NE:wdfdevice._WDF_DEVICE_POWER_STATE
title: "_WDF_DEVICE_POWER_STATE"
author: windows-driver-content
description: The WDF_DEVICE_POWER_STATE enumeration identifies all of the states that the framework's power state machine can enter.
old-location: wdf\wdf_device_power_state.htm
old-project: wdf
ms.assetid: 06bb6465-afc6-4b92-b3d7-1c66f6c6c33d
ms.author: windowsdriverdev
ms.date: 2/20/2018
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
product: Windows
targetos: Windows
req.typenames: WDF_DEVICE_POWER_STATE, *PWDF_DEVICE_POWER_STATE
req.product: Windows 10 or later.
---

# _WDF_DEVICE_POWER_STATE Enumeration
<p class="CCE_Message">[Applies to KMDF only]

The <b>WDF_DEVICE_POWER_STATE</b> enumeration identifies all of the states that the framework's power state machine can enter.

## Syntax
````
typedef enum _WDF_DEVICE_POWER_STATE { 
  WdfDevStatePowerInvalid                             = 0x00,
  WdfDevStatePowerObjectCreated                       = 0x300,
  WdfDevStatePowerCheckDeviceType                     = 0x301,
  WdfDevStatePowerCheckDeviceTypeNP                   = 0x302 | WdfDevStateNP,
  WdfDevStatePowerCheckParentState                    = 0x303,
  WdfDevStatePowerCheckParentStateNP                  = 0x304 | WdfDevStateNP,
  WdfDevStatePowerEnablingWakeAtBus                   = 0x305,
  WdfDevStatePowerEnablingWakeAtBusNP                 = 0x306 | WdfDevStateNP,
  WdfDevStatePowerD0                                  = 0x307,
  WdfDevStatePowerD0NP                                = 0x308 | WdfDevStateNP,
  WdfDevStatePowerD0BusWakeOwner                      = 0x309,
  WdfDevStatePowerD0BusWakeOwnerNP                    = 0x30A | WdfDevStateNP,
  WdfDevStatePowerD0ArmedForWake                      = 0x30B,
  WdfDevStatePowerD0ArmedForWakeNP                    = 0x30C | WdfDevStateNP,
  WdfDevStatePowerD0DisarmingWakeAtBus                = 0x30D,
  WdfDevStatePowerD0DisarmingWakeAtBusNP              = 0x30E | WdfDevStateNP,
  WdfDevStatePowerD0Starting                          = 0x30F,
  WdfDevStatePowerD0StartingConnectInterrupt          = 0x310,
  WdfDevStatePowerD0StartingDmaEnable                 = 0x311,
  WdfDevStatePowerD0StartingStartSelfManagedIo        = 0x312,
  WdfDevStatePowerDecideD0State                       = 0x313,
  WdfDevStatePowerGotoD3Stopped                       = 0x314,
  WdfDevStatePowerStopped                             = 0x315,
  WdfDevStatePowerStartingCheckDeviceType             = 0x316,
  WdfDevStatePowerStartingChild                       = 0x317,
  WdfDevStatePowerDxDisablingWakeAtBus                = 0x318,
  WdfDevStatePowerDxDisablingWakeAtBusNP              = 0x319 | WdfDevStateNP,
  WdfDevStatePowerGotoDx                              = 0x31A,
  WdfDevStatePowerGotoDxNP                            = 0x31B | WdfDevStateNP,
  WdfDevStatePowerGotoDxIoStopped                     = 0x31C,
  WdfDevStatePowerGotoDxIoStoppedNP                   = 0x31D | WdfDevStateNP,
  WdfDevStatePowerGotoDxNPFailed                      = 0x31E | WdfDevStateNP,
  WdfDevStatePowerDx                                  = 0x31F,
  WdfDevStatePowerDxNP                                = 0x320 | WdfDevStateNP,
  WdfDevStatePowerGotoDxArmedForWake                  = 0x321,
  WdfDevStatePowerGotoDxArmedForWakeNP                = 0x322 | WdfDevStateNP,
  WdfDevStatePowerGotoDxIoStoppedArmedForWake         = 0x323,
  WdfDevStatePowerGotoDxIoStoppedArmedForWakeNP       = 0x324 | WdfDevStateNP,
  WdfDevStatePowerDxArmedForWake                      = 0x325,
  WdfDevStatePowerDxArmedForWakeNP                    = 0x326 | WdfDevStateNP,
  WdfDevStatePowerCheckParentStateArmedForWake        = 0x327,
  WdfDevStatePowerCheckParentStateArmedForWakeNP      = 0x328 | WdfDevStateNP,
  WdfDevStatePowerWaitForParentArmedForWake           = 0x329,
  WdfDevStatePowerWaitForParentArmedForWakeNP         = 0x32A | WdfDevStateNP,
  WdfDevStatePowerStartSelfManagedIo                  = 0x32B,
  WdfDevStatePowerStartSelfManagedIoNP                = 0x32C | WdfDevStateNP,
  WdfDevStatePowerStartSelfManagedIoFailed            = 0x32D,
  WdfDevStatePowerStartSelfManagedIoFailedNP          = 0x32E | WdfDevStateNP,
  WdfDevStatePowerWaitForParent                       = 0x32F,
  WdfDevStatePowerWaitForParentNP                     = 0x330 | WdfDevStateNP,
  WdfDevStatePowerWakePending                         = 0x331,
  WdfDevStatePowerWakePendingNP                       = 0x332 | WdfDevStateNP,
  WdfDevStatePowerWaking                              = 0x333,
  WdfDevStatePowerWakingNP                            = 0x334 | WdfDevStateNP,
  WdfDevStatePowerWakingConnectInterrupt              = 0x335,
  WdfDevStatePowerWakingConnectInterruptNP            = 0x336 | WdfDevStateNP,
  WdfDevStatePowerWakingConnectInterruptFailed        = 0x337,
  WdfDevStatePowerWakingConnectInterruptFailedNP      = 0x338 | WdfDevStateNP,
  WdfDevStatePowerWakingDmaEnable                     = 0x339,
  WdfDevStatePowerWakingDmaEnableNP                   = 0x33A | WdfDevStateNP,
  WdfDevStatePowerWakingDmaEnableFailed               = 0x33B,
  WdfDevStatePowerWakingDmaEnableFailedNP             = 0x33C | WdfDevStateNP,
  WdfDevStatePowerReportPowerUpFailedDerefParent      = 0x33D,
  WdfDevStatePowerReportPowerUpFailed                 = 0x33E,
  WdfDevStatePowerPowerFailedPowerDown                = 0x33F,
  WdfDevStatePowerReportPowerDownFailed               = 0x340,
  WdfDevStatePowerInitialConnectInterruptFailed       = 0x341,
  WdfDevStatePowerInitialDmaEnableFailed              = 0x342,
  WdfDevStatePowerInitialSelfManagedIoFailed          = 0x343,
  WdfDevStatePowerInitialPowerUpFailedDerefParent     = 0x344,
  WdfDevStatePowerInitialPowerUpFailed                = 0x345,
  WdfDevStatePowerDxStoppedDisarmWake                 = 0x346,
  WdfDevStatePowerDxStoppedDisarmWakeNP               = 0x347 | WdfDevStateNP,
  WdfDevStatePowerGotoDxStoppedDisableInterruptNP     = 0x348 | WdfDevStateNP,
  WdfDevStatePowerGotoDxStopped                       = 0x349,
  WdfDevStatePowerDxStopped                           = 0x34A,
  WdfDevStatePowerGotoStopped                         = 0x34B,
  WdfDevStatePowerStoppedCompleteDx                   = 0x34C,
  WdfDevStatePowerDxStoppedDecideDxState              = 0x34D,
  WdfDevStatePowerDxStoppedArmForWake                 = 0x34E,
  WdfDevStatePowerDxStoppedArmForWakeNP               = 0x34F | WdfDevStateNP,
  WdfDevStatePowerFinalPowerDownFailed                = 0x350,
  WdfDevStatePowerFinal                               = 0x351,
  WdfDevStatePowerGotoImplicitD3DisarmWakeAtBus       = 0x352,
  WdfDevStatePowerUpFailed                            = 0x353,
  WdfDevStatePowerUpFailedDerefParent                 = 0x354,
  WdfDevStatePowerGotoDxFailed                        = 0x355,
  WdfDevStatePowerGotoDxStoppedDisableInterrupt       = 0x356,
  WdfDevStatePowerUpFailedNP                          = 0x357 | WdfDevStateNP,
  WdfDevStatePowerUpFailedDerefParentNP               = 0x358 | WdfDevStateNP,
  WdfDevStatePowerNotifyingD0ExitToWakeInterrupts     = 0x359,
  WdfDevStatePowerNotifyingD0EntryToWakeInterrupts    = 0x35A,
  WdfDevStatePowerNotifyingD0ExitToWakeInterruptsNP   = 0x35B | WdfDevStateNP,
  WdfDevStatePowerNotifyingD0EntryToWakeInterruptsNP  = 0x35C | WdfDevStateNP,
  WdfDevStatePowerInitialPowerUpFailedPowerDown       = 0x35D,
  WdfDevStatePowerUpFailedPowerDown                   = 0x35E,
  WdfDevStatePowerUpFailedPowerDownNP                 = 0x35F | WdfDevStateNP,
  WdfDevStatePowerInitialSelfManagedIoFailedStarted   = 0x360,
  WdfDevStatePowerStartSelfManagedIoFailedStarted     = 0x361,
  WdfDevStatePowerStartSelfManagedIoFailedStartedNP   = 0x362 | WdfDevStateNP,
  WdfDevStatePowerNull                                = 0x363
} WDF_DEVICE_POWER_STATE, *PWDF_DEVICE_POWER_STATE;
````

## Constants

<table>
            
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
                    <td>WdfDevStatePowerCheckParentStateArmedForWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerCheckParentStateArmedForWakeNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerCheckParentStateNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0</td>
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
                    <td>WdfDevStatePowerD0BusWakeOwner</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerD0BusWakeOwnerNP</td>
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
                    <td>WdfDevStatePowerD0NP</td>
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
                    <td>WdfDevStatePowerDx</td>
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
                    <td>WdfDevStatePowerDxDisablingWakeAtBus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxDisablingWakeAtBusNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerDxStopped</td>
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
                    <td>WdfDevStatePowerDxStoppedDecideDxState</td>
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
                    <td>WdfDevStatePowerEnablingWakeAtBus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerEnablingWakeAtBusNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerFinal</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerFinalPowerDownFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoD3Stopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDx</td>
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
                    <td>WdfDevStatePowerGotoDxFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxIoStopped</td>
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
                    <td>WdfDevStatePowerGotoDxIoStoppedNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxNPFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxStopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxStoppedDisableInterrupt</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoDxStoppedDisableInterruptNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoImplicitD3DisarmWakeAtBus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerGotoStopped</td>
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
                    <td>WdfDevStatePowerInitialPowerUpFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInitialPowerUpFailedDerefParent</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInitialPowerUpFailedPowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInitialSelfManagedIoFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInitialSelfManagedIoFailedStarted</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerInvalid</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerNotifyingD0EntryToWakeInterrupts</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerNotifyingD0EntryToWakeInterruptsNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerNotifyingD0ExitToWakeInterrupts</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerNotifyingD0ExitToWakeInterruptsNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerNull</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerObjectCreated</td>
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
                    <td>WdfDevStatePowerReportPowerUpFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerReportPowerUpFailedDerefParent</td>
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
                    <td>WdfDevStatePowerStartSelfManagedIo</td>
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
                    <td>WdfDevStatePowerStartSelfManagedIoFailedStarted</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStartSelfManagedIoFailedStartedNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStartSelfManagedIoNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerStoppedCompleteDx</td>
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
                    <td>WdfDevStatePowerUpFailedDerefParentNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerUpFailedNP</td>
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
                    <td>WdfDevStatePowerWaitForParent</td>
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
                    <td>WdfDevStatePowerWakingConnectInterrupt</td>
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
                    <td>WdfDevStatePowerWakingConnectInterruptNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakingDmaEnable</td>
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
                    <td>WdfDevStatePowerWakingDmaEnableNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePowerWakingNP</td>
                    <td></td>
                </tr>
</table>

## Remarks

The <b>WDF_DEVICE_POWER_STATE</b> enumeration is used as a member type in the <a href="..\wdfdevice\ns-wdfdevice-_wdf_device_power_notification_data.md">WDF_DEVICE_POWER_NOTIFICATION_DATA</a> structure and as the return type for the <a href="..\wdfdevice\nf-wdfdevice-wdfdevicegetdevicepowerstate.md">WdfDeviceGetDevicePowerState</a> method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Header** | wdfdevice.h (include Wdf.h) |