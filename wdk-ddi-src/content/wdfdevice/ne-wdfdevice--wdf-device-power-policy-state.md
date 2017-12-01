---
UID: NE.wdfdevice._WDF_DEVICE_POWER_POLICY_STATE
title: WDF_DEVICE_POWER_POLICY_STATE
author: windows-driver-content
description: The WDF_DEVICE_POWER_POLICY_STATE enumeration identifies all of the states that the framework's power policy state machine can enter.
old-location: wdf\wdf_device_power_policy_state.htm
old-project: wdf
ms.assetid: 87fa78f7-417a-4720-9520-0eb90486630a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
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
req.alt-api: WDF_DEVICE_POWER_POLICY_STATE
req.alt-loc: wdfdevice.h
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
req.product: Windows 10 or later.
---

# WDF_DEVICE_POWER_POLICY_STATE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The WDF_DEVICE_POWER_POLICY_STATE enumeration identifies all of the states that the framework's power policy state machine can enter.</p>


## -syntax

````
typedef enum _WDF_DEVICE_POWER_POLICY_STATE { 
  WdfDevStatePwrPolInvalid                                                     = 0x00,
  WdfDevStatePwrPolObjectCreated                                               = 0x500,
  WdfDevStatePwrPolStarting                                                    = 0x501,
  WdfDevStatePwrPolStartingSucceeded                                           = 0x502,
  WdfDevStatePwrPolStartingFailed                                              = 0x503,
  WdfDevStatePwrPolStartingDecideS0Wake                                        = 0x504,
  WdfDevStatePwrPolStartedIdleCapable                                          = 0x505,
  WdfDevStatePwrPolTimerExpiredNoWake                                          = 0x506,
  WdfDevStatePwrPolTimerExpiredNoWakeCompletePowerDown                         = 0x507,
  WdfDevStatePwrPolWaitingUnarmed                                              = 0x508,
  WdfDevStatePwrPolWaitingUnarmedQueryIdle                                     = 0x509,
  WdfDevStatePwrPolS0NoWakePowerUp                                             = 0x50A,
  WdfDevStatePwrPolS0NoWakeCompletePowerUp                                     = 0x50B,
  WdfDevStatePwrPolSystemSleepFromDeviceWaitingUnarmed                         = 0x50C,
  WdfDevStatePwrPolSystemSleepNeedWake                                         = 0x50D,
  WdfDevStatePwrPolSystemSleepNeedWakeCompletePowerUp                          = 0x50E,
  WdfDevStatePwrPolSystemSleepPowerRequestFailed                               = 0x50F,
  WdfDevStatePwrPolCheckPowerPageable                                          = 0x510,
  WdfDevStatePwrPolSleepingWakeWakeArrived                                     = 0x511,
  WdfDevStatePwrPolSleepingWakeRevertArmWake                                   = 0x512,
  WdfDevStatePwrPolSystemAsleepWakeArmed                                       = 0x513,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabled                                 = 0x514,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceled                     = 0x515,
  WdfDevStatePwrPolSystemWakeDeviceWakeDisarm                                  = 0x516,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggered                               = 0x517,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0                             = 0x518,
  WdfDevStatePwrPolSystemWakeDeviceWokeDisarm                                  = 0x519,
  WdfDevStatePwrPolSleepingWakeWakeArrivedNP                                   = 0x51A | WdfDevStateNP,
  WdfDevStatePwrPolSleepingWakeRevertArmWakeNP                                 = 0x51B | WdfDevStateNP,
  WdfDevStatePwrPolSleepingWakePowerDownFailed                                 = 0x51C,
  WdfDevStatePwrPolSleepingWakePowerDownFailedWakeCanceled                     = 0x51D,
  WdfDevStatePwrPolSystemAsleepWakeArmedNP                                     = 0x51E | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabledNP                               = 0x51F | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceledNP                   = 0x520 | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeDisarmNP                                = 0x521 | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredNP                             = 0x522 | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0NP                           = 0x523 | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWokeDisarmNP                                = 0x524 | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeCompletePowerUp                         = 0x525,
  WdfDevStatePwrPolSleeping                                                    = 0x526,
  WdfDevStatePwrPolSleepingNoWakePowerDown                                     = 0x527,
  WdfDevStatePwrPolSleepingNoWakeCompletePowerDown                             = 0x528,
  WdfDevStatePwrPolSleepingNoWakeDxRequestFailed                               = 0x529,
  WdfDevStatePwrPolSleepingWakePowerDown                                       = 0x52A,
  WdfDevStatePwrPolSleepingSendWake                                            = 0x52B,
  WdfDevStatePwrPolSystemAsleepNoWake                                          = 0x52C,
  WdfDevStatePwrPolSystemWakeDeviceWakeDisabled                                = 0x52D,
  WdfDevStatePwrPolSystemWakeDeviceToD0                                        = 0x52E,
  WdfDevStatePwrPolSystemWakeDeviceToD0CompletePowerUp                         = 0x52F,
  WdfDevStatePwrPolSystemWakeQueryIdle                                         = 0x530,
  WdfDevStatePwrPolStartedWakeCapable                                          = 0x531,
  WdfDevStatePwrPolTimerExpiredDecideUsbSS                                     = 0x532,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDown                            = 0x533,
  WdfDevStatePwrPolTimerExpiredWakeCapableSendWake                             = 0x534,
  WdfDevStatePwrPolTimerExpiredWakeCapableUsbSS                                = 0x535,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeArrived                          = 0x536,
  WdfDevStatePwrPolTimerExpiredWakeCapableCancelWake                           = 0x537,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeCanceled                         = 0x538,
  WdfDevStatePwrPolTimerExpiredWakeCapableCleanup                              = 0x539,
  WdfDevStatePwrPolTimerExpiredWakeCapableDxAllocFailed                        = 0x53A,
  WdfDevStatePwrPolTimerExpiredWakeCompletedPowerDown                          = 0x53B,
  WdfDevStatePwrPolTimerExpiredWakeCompletedPowerUp                            = 0x53C,
  WdfDevStatePwrPolWaitingArmedUsbSS                                           = 0x53D,
  WdfDevStatePwrPolWaitingArmed                                                = 0x53E,
  WdfDevStatePwrPolWaitingArmedQueryIdle                                       = 0x53F,
  WdfDevStatePwrPolIoPresentArmed                                              = 0x540,
  WdfDevStatePwrPolIoPresentArmedWakeCanceled                                  = 0x541,
  WdfDevStatePwrPolS0WakeDisarm                                                = 0x542,
  WdfDevStatePwrPolS0WakeCompletePowerUp                                       = 0x543,
  WdfDevStatePwrPolTimerExpiredWakeSucceeded                                   = 0x544,
  WdfDevStatePwrPolTimerExpiredWakeCompletedDisarm                             = 0x545,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeSucceeded                        = 0x546,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeFailed                           = 0x547,
  WdfDevStatePwrPolWakeFailedUsbSS                                             = 0x548,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedCancelWake            = 0x549,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeCanceled          = 0x54A,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedUsbSS                 = 0x54B,
  WdfDevStatePwrPolCancelingWakeForSystemSleep                                 = 0x54C,
  WdfDevStatePwrPolCancelingWakeForSystemSleepWakeCanceled                     = 0x54D,
  WdfDevStatePwrPolDisarmingWakeForSystemSleepCompletePowerUp                  = 0x54E,
  WdfDevStatePwrPolPowerUpForSystemSleepFailed                                 = 0x54F,
  WdfDevStatePwrPolWokeFromS0UsbSS                                             = 0x550,
  WdfDevStatePwrPolWokeFromS0                                                  = 0x551,
  WdfDevStatePwrPolWokeFromS0NotifyDriver                                      = 0x552,
  WdfDevStatePwrPolStoppingResetDevice                                         = 0x553,
  WdfDevStatePwrPolStoppingResetDeviceCompletePowerUp                          = 0x554,
  WdfDevStatePwrPolStoppingResetDeviceFailed                                   = 0x555,
  WdfDevStatePwrPolStoppingD0                                                  = 0x556,
  WdfDevStatePwrPolStoppingD0Failed                                            = 0x557,
  WdfDevStatePwrPolStoppingDisarmWake                                          = 0x558,
  WdfDevStatePwrPolStoppingDisarmWakeCancelWake                                = 0x559,
  WdfDevStatePwrPolStoppingDisarmWakeWakeCanceled                              = 0x55A,
  WdfDevStatePwrPolStopping                                                    = 0x55B,
  WdfDevStatePwrPolStoppingFailed                                              = 0x55C,
  WdfDevStatePwrPolStoppingSendStatus                                          = 0x55D,
  WdfDevStatePwrPolStoppingCancelTimer                                         = 0x55E,
  WdfDevStatePwrPolStoppingWaitForIdleTimeout                                  = 0x55F,
  WdfDevStatePwrPolStoppingCancelUsbSS                                         = 0x560,
  WdfDevStatePwrPolStoppingWaitForUsbSSCompletion                              = 0x561,
  WdfDevStatePwrPolStoppingCancelWake                                          = 0x562,
  WdfDevStatePwrPolStopped                                                     = 0x563,
  WdfDevStatePwrPolCancelUsbSS                                                 = 0x564,
  WdfDevStatePwrPolStarted                                                     = 0x565,
  WdfDevStatePwrPolStartedCancelTimer                                          = 0x566,
  WdfDevStatePwrPolStartedWaitForIdleTimeout                                   = 0x567,
  WdfDevStatePwrPolStartedWakeCapableCancelTimerForSleep                       = 0x568,
  WdfDevStatePwrPolStartedWakeCapableWaitForIdleTimeout                        = 0x569,
  WdfDevStatePwrPolStartedWakeCapableSleepingUsbSS                             = 0x56A,
  WdfDevStatePwrPolStartedIdleCapableCancelTimerForSleep                       = 0x56B,
  WdfDevStatePwrPolStartedIdleCapableWaitForIdleTimeout                        = 0x56C,
  WdfDevStatePwrPolDeviceD0PowerRequestFailed                                  = 0x56D,
  WdfDevStatePwrPolDevicePowerRequestFailed                                    = 0x56E,
  WdfDevStatePwrPolGotoDx                                                      = 0x56F,
  WdfDevStatePwrPolGotoDxInDx                                                  = 0x570,
  WdfDevStatePwrPolDx                                                          = 0x571,
  WdfDevStatePwrPolGotoD0                                                      = 0x572,
  WdfDevStatePwrPolGotoD0InD0                                                  = 0x573,
  WdfDevStatePwrPolFinal                                                       = 0x574,
  WdfDevStatePwrPolSleepingPowerDownNotProcessed                               = 0x575,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownNotProcessed                = 0x576,
  WdfDevStatePwrPolTimerExpiredNoWakePowerDownNotProcessed                     = 0x577,
  WdfDevStatePwrPolTimerExpiredNoWakePoweredDownDisableIdleTimer               = 0x578,
  WdfDevStatePwrPolStoppingWaitingForImplicitPowerDown                         = 0x579,
  WdfDevStatePwrPolStoppingPoweringUp                                          = 0x57A,
  WdfDevStatePwrPolStoppingPoweringDown                                        = 0x57B,
  WdfDevStatePwrPolPowerUpForSystemSleepNotSeen                                = 0x57C,
  WdfDevStatePwrPolWaitingArmedStoppingCancelUsbSS                             = 0x57D,
  WdfDevStatePwrPolWaitingArmedWakeFailedCancelUsbSS                           = 0x57E,
  WdfDevStatePwrPolWaitingArmedIoPresentCancelUsbSS                            = 0x57F,
  WdfDevStatePwrPolWaitingArmedWakeSucceededCancelUsbSS                        = 0x580,
  WdfDevStatePwrPolCancelingUsbSSForSystemSleep                                = 0x581,
  WdfDevStatePwrPolStoppingD0CancelUsbSS                                       = 0x582,
  WdfDevStatePwrPolStartingPoweredUp                                           = 0x583,
  WdfDevStatePwrPolIdleCapableDeviceIdle                                       = 0x584,
  WdfDevStatePwrPolDeviceIdleReturnToActive                                    = 0x585,
  WdfDevStatePwrPolDeviceIdleSleeping                                          = 0x586,
  WdfDevStatePwrPolDeviceIdleStopping                                          = 0x587,
  WdfDevStatePwrPolTimerExpiredNoWakeUndoPowerDown                             = 0x588,
  WdfDevStatePwrPolWakeCapableDeviceIdle                                       = 0x589,
  WdfDevStatePwrPolWakeCapableUsbSSCompleted                                   = 0x58A,
  WdfDevStatePwrPolTimerExpiredWakeCapableUndoPowerDown                        = 0x58B,
  WdfDevStatePwrPolTimerExpiredWakeCompletedHardwareStarted                    = 0x58C,
  WdfDevStatePwrPolStoppedRemoving                                             = 0x58D,
  WdfDevStatePwrPolRemoved                                                     = 0x58E,
  WdfDevStatePwrPolRestarting                                                  = 0x58F,
  WdfDevStatePwrPolRestartingFailed                                            = 0x590,
  WdfDevStatePwrPolStartingPoweredUpFailed                                     = 0x591,
  WdfDevStatePwrPolTimerExpiredNoWakeReturnToActive                            = 0x592,
  WdfDevStatePwrPolWaitingArmedWakeInterruptFired                              = 0x593,
  WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFired                          = 0x594,
  WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFiredNP                        = 0x595 | WdfDevStateNP,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeInterruptArrived                 = 0x596,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeInterruptArrived  = 0x597,
  WdfDevStatePwrPolWaitingArmedWakeInterruptFiredDuringPowerDown               = 0x598,
  WdfDevStatePwrPolNull                                                        = 0x599
} WDF_DEVICE_POWER_POLICY_STATE, *PWDF_DEVICE_POWER_POLICY_STATE;
````


## -enum-fields
<dl>

### -field <a id="WdfDevStatePwrPolInvalid"></a><a id="wdfdevstatepwrpolinvalid"></a><a id="WDFDEVSTATEPWRPOLINVALID"></a><b>WdfDevStatePwrPolInvalid</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolObjectCreated"></a><a id="wdfdevstatepwrpolobjectcreated"></a><a id="WDFDEVSTATEPWRPOLOBJECTCREATED"></a><b>WdfDevStatePwrPolObjectCreated</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStarting"></a><a id="wdfdevstatepwrpolstarting"></a><a id="WDFDEVSTATEPWRPOLSTARTING"></a><b>WdfDevStatePwrPolStarting</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartingSucceeded"></a><a id="wdfdevstatepwrpolstartingsucceeded"></a><a id="WDFDEVSTATEPWRPOLSTARTINGSUCCEEDED"></a><b>WdfDevStatePwrPolStartingSucceeded</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartingFailed"></a><a id="wdfdevstatepwrpolstartingfailed"></a><a id="WDFDEVSTATEPWRPOLSTARTINGFAILED"></a><b>WdfDevStatePwrPolStartingFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartingDecideS0Wake"></a><a id="wdfdevstatepwrpolstartingdecides0wake"></a><a id="WDFDEVSTATEPWRPOLSTARTINGDECIDES0WAKE"></a><b>WdfDevStatePwrPolStartingDecideS0Wake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartedIdleCapable"></a><a id="wdfdevstatepwrpolstartedidlecapable"></a><a id="WDFDEVSTATEPWRPOLSTARTEDIDLECAPABLE"></a><b>WdfDevStatePwrPolStartedIdleCapable</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredNoWake"></a><a id="wdfdevstatepwrpoltimerexpirednowake"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDNOWAKE"></a><b>WdfDevStatePwrPolTimerExpiredNoWake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredNoWakeCompletePowerDown"></a><a id="wdfdevstatepwrpoltimerexpirednowakecompletepowerdown"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDNOWAKECOMPLETEPOWERDOWN"></a><b>WdfDevStatePwrPolTimerExpiredNoWakeCompletePowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWaitingUnarmed"></a><a id="wdfdevstatepwrpolwaitingunarmed"></a><a id="WDFDEVSTATEPWRPOLWAITINGUNARMED"></a><b>WdfDevStatePwrPolWaitingUnarmed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWaitingUnarmedQueryIdle"></a><a id="wdfdevstatepwrpolwaitingunarmedqueryidle"></a><a id="WDFDEVSTATEPWRPOLWAITINGUNARMEDQUERYIDLE"></a><b>WdfDevStatePwrPolWaitingUnarmedQueryIdle</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolS0NoWakePowerUp"></a><a id="wdfdevstatepwrpols0nowakepowerup"></a><a id="WDFDEVSTATEPWRPOLS0NOWAKEPOWERUP"></a><b>WdfDevStatePwrPolS0NoWakePowerUp</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolS0NoWakeCompletePowerUp"></a><a id="wdfdevstatepwrpols0nowakecompletepowerup"></a><a id="WDFDEVSTATEPWRPOLS0NOWAKECOMPLETEPOWERUP"></a><b>WdfDevStatePwrPolS0NoWakeCompletePowerUp</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemSleepFromDeviceWaitingUnarmed"></a><a id="wdfdevstatepwrpolsystemsleepfromdevicewaitingunarmed"></a><a id="WDFDEVSTATEPWRPOLSYSTEMSLEEPFROMDEVICEWAITINGUNARMED"></a><b>WdfDevStatePwrPolSystemSleepFromDeviceWaitingUnarmed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemSleepNeedWake"></a><a id="wdfdevstatepwrpolsystemsleepneedwake"></a><a id="WDFDEVSTATEPWRPOLSYSTEMSLEEPNEEDWAKE"></a><b>WdfDevStatePwrPolSystemSleepNeedWake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemSleepNeedWakeCompletePowerUp"></a><a id="wdfdevstatepwrpolsystemsleepneedwakecompletepowerup"></a><a id="WDFDEVSTATEPWRPOLSYSTEMSLEEPNEEDWAKECOMPLETEPOWERUP"></a><b>WdfDevStatePwrPolSystemSleepNeedWakeCompletePowerUp</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemSleepPowerRequestFailed"></a><a id="wdfdevstatepwrpolsystemsleeppowerrequestfailed"></a><a id="WDFDEVSTATEPWRPOLSYSTEMSLEEPPOWERREQUESTFAILED"></a><b>WdfDevStatePwrPolSystemSleepPowerRequestFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolCheckPowerPageable"></a><a id="wdfdevstatepwrpolcheckpowerpageable"></a><a id="WDFDEVSTATEPWRPOLCHECKPOWERPAGEABLE"></a><b>WdfDevStatePwrPolCheckPowerPageable</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingWakeWakeArrived"></a><a id="wdfdevstatepwrpolsleepingwakewakearrived"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGWAKEWAKEARRIVED"></a><b>WdfDevStatePwrPolSleepingWakeWakeArrived</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingWakeRevertArmWake"></a><a id="wdfdevstatepwrpolsleepingwakerevertarmwake"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGWAKEREVERTARMWAKE"></a><b>WdfDevStatePwrPolSleepingWakeRevertArmWake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemAsleepWakeArmed"></a><a id="wdfdevstatepwrpolsystemasleepwakearmed"></a><a id="WDFDEVSTATEPWRPOLSYSTEMASLEEPWAKEARMED"></a><b>WdfDevStatePwrPolSystemAsleepWakeArmed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeEnabled"></a><a id="wdfdevstatepwrpolsystemwakedevicewakeenabled"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKEENABLED"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeEnabled</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceled"></a><a id="wdfdevstatepwrpolsystemwakedevicewakeenabledwakecanceled"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKEENABLEDWAKECANCELED"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceled</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeDisarm"></a><a id="wdfdevstatepwrpolsystemwakedevicewakedisarm"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKEDISARM"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeDisarm</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeTriggered"></a><a id="wdfdevstatepwrpolsystemwakedevicewaketriggered"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKETRIGGERED"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeTriggered</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0"></a><a id="wdfdevstatepwrpolsystemwakedevicewaketriggereds0"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKETRIGGEREDS0"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWokeDisarm"></a><a id="wdfdevstatepwrpolsystemwakedevicewokedisarm"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWOKEDISARM"></a><b>WdfDevStatePwrPolSystemWakeDeviceWokeDisarm</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingWakeWakeArrivedNP"></a><a id="wdfdevstatepwrpolsleepingwakewakearrivednp"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGWAKEWAKEARRIVEDNP"></a><b>WdfDevStatePwrPolSleepingWakeWakeArrivedNP</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingWakeRevertArmWakeNP"></a><a id="wdfdevstatepwrpolsleepingwakerevertarmwakenp"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGWAKEREVERTARMWAKENP"></a><b>WdfDevStatePwrPolSleepingWakeRevertArmWakeNP</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingWakePowerDownFailed"></a><a id="wdfdevstatepwrpolsleepingwakepowerdownfailed"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGWAKEPOWERDOWNFAILED"></a><b>WdfDevStatePwrPolSleepingWakePowerDownFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingWakePowerDownFailedWakeCanceled"></a><a id="wdfdevstatepwrpolsleepingwakepowerdownfailedwakecanceled"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGWAKEPOWERDOWNFAILEDWAKECANCELED"></a><b>WdfDevStatePwrPolSleepingWakePowerDownFailedWakeCanceled</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemAsleepWakeArmedNP"></a><a id="wdfdevstatepwrpolsystemasleepwakearmednp"></a><a id="WDFDEVSTATEPWRPOLSYSTEMASLEEPWAKEARMEDNP"></a><b>WdfDevStatePwrPolSystemAsleepWakeArmedNP</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeEnabledNP"></a><a id="wdfdevstatepwrpolsystemwakedevicewakeenablednp"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKEENABLEDNP"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeEnabledNP</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceledNP"></a><a id="wdfdevstatepwrpolsystemwakedevicewakeenabledwakecancelednp"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKEENABLEDWAKECANCELEDNP"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceledNP</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeDisarmNP"></a><a id="wdfdevstatepwrpolsystemwakedevicewakedisarmnp"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKEDISARMNP"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeDisarmNP</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredNP"></a><a id="wdfdevstatepwrpolsystemwakedevicewaketriggerednp"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKETRIGGEREDNP"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredNP</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0NP"></a><a id="wdfdevstatepwrpolsystemwakedevicewaketriggereds0np"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKETRIGGEREDS0NP"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0NP</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWokeDisarmNP"></a><a id="wdfdevstatepwrpolsystemwakedevicewokedisarmnp"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWOKEDISARMNP"></a><b>WdfDevStatePwrPolSystemWakeDeviceWokeDisarmNP</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeCompletePowerUp"></a><a id="wdfdevstatepwrpolsystemwakedevicewakecompletepowerup"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKECOMPLETEPOWERUP"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeCompletePowerUp</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleeping"></a><a id="wdfdevstatepwrpolsleeping"></a><a id="WDFDEVSTATEPWRPOLSLEEPING"></a><b>WdfDevStatePwrPolSleeping</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingNoWakePowerDown"></a><a id="wdfdevstatepwrpolsleepingnowakepowerdown"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGNOWAKEPOWERDOWN"></a><b>WdfDevStatePwrPolSleepingNoWakePowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingNoWakeCompletePowerDown"></a><a id="wdfdevstatepwrpolsleepingnowakecompletepowerdown"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGNOWAKECOMPLETEPOWERDOWN"></a><b>WdfDevStatePwrPolSleepingNoWakeCompletePowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingNoWakeDxRequestFailed"></a><a id="wdfdevstatepwrpolsleepingnowakedxrequestfailed"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGNOWAKEDXREQUESTFAILED"></a><b>WdfDevStatePwrPolSleepingNoWakeDxRequestFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingWakePowerDown"></a><a id="wdfdevstatepwrpolsleepingwakepowerdown"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGWAKEPOWERDOWN"></a><b>WdfDevStatePwrPolSleepingWakePowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingSendWake"></a><a id="wdfdevstatepwrpolsleepingsendwake"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGSENDWAKE"></a><b>WdfDevStatePwrPolSleepingSendWake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemAsleepNoWake"></a><a id="wdfdevstatepwrpolsystemasleepnowake"></a><a id="WDFDEVSTATEPWRPOLSYSTEMASLEEPNOWAKE"></a><b>WdfDevStatePwrPolSystemAsleepNoWake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeDisabled"></a><a id="wdfdevstatepwrpolsystemwakedevicewakedisabled"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKEDISABLED"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeDisabled</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceToD0"></a><a id="wdfdevstatepwrpolsystemwakedevicetod0"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICETOD0"></a><b>WdfDevStatePwrPolSystemWakeDeviceToD0</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceToD0CompletePowerUp"></a><a id="wdfdevstatepwrpolsystemwakedevicetod0completepowerup"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICETOD0COMPLETEPOWERUP"></a><b>WdfDevStatePwrPolSystemWakeDeviceToD0CompletePowerUp</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeQueryIdle"></a><a id="wdfdevstatepwrpolsystemwakequeryidle"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEQUERYIDLE"></a><b>WdfDevStatePwrPolSystemWakeQueryIdle</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartedWakeCapable"></a><a id="wdfdevstatepwrpolstartedwakecapable"></a><a id="WDFDEVSTATEPWRPOLSTARTEDWAKECAPABLE"></a><b>WdfDevStatePwrPolStartedWakeCapable</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredDecideUsbSS"></a><a id="wdfdevstatepwrpoltimerexpireddecideusbss"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDDECIDEUSBSS"></a><b>WdfDevStatePwrPolTimerExpiredDecideUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapablePowerDown"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablepowerdown"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEPOWERDOWN"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapableSendWake"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablesendwake"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLESENDWAKE"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapableSendWake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapableUsbSS"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapableusbss"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEUSBSS"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapableUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapableWakeArrived"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablewakearrived"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEWAKEARRIVED"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapableWakeArrived</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapableCancelWake"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablecancelwake"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLECANCELWAKE"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapableCancelWake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapableWakeCanceled"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablewakecanceled"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEWAKECANCELED"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapableWakeCanceled</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapableCleanup"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablecleanup"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLECLEANUP"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapableCleanup</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapableDxAllocFailed"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapabledxallocfailed"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEDXALLOCFAILED"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapableDxAllocFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCompletedPowerDown"></a><a id="wdfdevstatepwrpoltimerexpiredwakecompletedpowerdown"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECOMPLETEDPOWERDOWN"></a><b>WdfDevStatePwrPolTimerExpiredWakeCompletedPowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCompletedPowerUp"></a><a id="wdfdevstatepwrpoltimerexpiredwakecompletedpowerup"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECOMPLETEDPOWERUP"></a><b>WdfDevStatePwrPolTimerExpiredWakeCompletedPowerUp</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWaitingArmedUsbSS"></a><a id="wdfdevstatepwrpolwaitingarmedusbss"></a><a id="WDFDEVSTATEPWRPOLWAITINGARMEDUSBSS"></a><b>WdfDevStatePwrPolWaitingArmedUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWaitingArmed"></a><a id="wdfdevstatepwrpolwaitingarmed"></a><a id="WDFDEVSTATEPWRPOLWAITINGARMED"></a><b>WdfDevStatePwrPolWaitingArmed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWaitingArmedQueryIdle"></a><a id="wdfdevstatepwrpolwaitingarmedqueryidle"></a><a id="WDFDEVSTATEPWRPOLWAITINGARMEDQUERYIDLE"></a><b>WdfDevStatePwrPolWaitingArmedQueryIdle</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolIoPresentArmed"></a><a id="wdfdevstatepwrpoliopresentarmed"></a><a id="WDFDEVSTATEPWRPOLIOPRESENTARMED"></a><b>WdfDevStatePwrPolIoPresentArmed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolIoPresentArmedWakeCanceled"></a><a id="wdfdevstatepwrpoliopresentarmedwakecanceled"></a><a id="WDFDEVSTATEPWRPOLIOPRESENTARMEDWAKECANCELED"></a><b>WdfDevStatePwrPolIoPresentArmedWakeCanceled</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolS0WakeDisarm"></a><a id="wdfdevstatepwrpols0wakedisarm"></a><a id="WDFDEVSTATEPWRPOLS0WAKEDISARM"></a><b>WdfDevStatePwrPolS0WakeDisarm</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolS0WakeCompletePowerUp"></a><a id="wdfdevstatepwrpols0wakecompletepowerup"></a><a id="WDFDEVSTATEPWRPOLS0WAKECOMPLETEPOWERUP"></a><b>WdfDevStatePwrPolS0WakeCompletePowerUp</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeSucceeded"></a><a id="wdfdevstatepwrpoltimerexpiredwakesucceeded"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKESUCCEEDED"></a><b>WdfDevStatePwrPolTimerExpiredWakeSucceeded</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCompletedDisarm"></a><a id="wdfdevstatepwrpoltimerexpiredwakecompleteddisarm"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECOMPLETEDDISARM"></a><b>WdfDevStatePwrPolTimerExpiredWakeCompletedDisarm</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapableWakeSucceeded"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablewakesucceeded"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEWAKESUCCEEDED"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapableWakeSucceeded</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapableWakeFailed"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablewakefailed"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEWAKEFAILED"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapableWakeFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWakeFailedUsbSS"></a><a id="wdfdevstatepwrpolwakefailedusbss"></a><a id="WDFDEVSTATEPWRPOLWAKEFAILEDUSBSS"></a><b>WdfDevStatePwrPolWakeFailedUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedCancelWake"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablepowerdownfailedcancelwake"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEPOWERDOWNFAILEDCANCELWAKE"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedCancelWake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeCanceled"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablepowerdownfailedwakecanceled"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEPOWERDOWNFAILEDWAKECANCELED"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeCanceled</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedUsbSS"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablepowerdownfailedusbss"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEPOWERDOWNFAILEDUSBSS"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolCancelingWakeForSystemSleep"></a><a id="wdfdevstatepwrpolcancelingwakeforsystemsleep"></a><a id="WDFDEVSTATEPWRPOLCANCELINGWAKEFORSYSTEMSLEEP"></a><b>WdfDevStatePwrPolCancelingWakeForSystemSleep</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolCancelingWakeForSystemSleepWakeCanceled"></a><a id="wdfdevstatepwrpolcancelingwakeforsystemsleepwakecanceled"></a><a id="WDFDEVSTATEPWRPOLCANCELINGWAKEFORSYSTEMSLEEPWAKECANCELED"></a><b>WdfDevStatePwrPolCancelingWakeForSystemSleepWakeCanceled</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolDisarmingWakeForSystemSleepCompletePowerUp"></a><a id="wdfdevstatepwrpoldisarmingwakeforsystemsleepcompletepowerup"></a><a id="WDFDEVSTATEPWRPOLDISARMINGWAKEFORSYSTEMSLEEPCOMPLETEPOWERUP"></a><b>WdfDevStatePwrPolDisarmingWakeForSystemSleepCompletePowerUp</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolPowerUpForSystemSleepFailed"></a><a id="wdfdevstatepwrpolpowerupforsystemsleepfailed"></a><a id="WDFDEVSTATEPWRPOLPOWERUPFORSYSTEMSLEEPFAILED"></a><b>WdfDevStatePwrPolPowerUpForSystemSleepFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWokeFromS0UsbSS"></a><a id="wdfdevstatepwrpolwokefroms0usbss"></a><a id="WDFDEVSTATEPWRPOLWOKEFROMS0USBSS"></a><b>WdfDevStatePwrPolWokeFromS0UsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWokeFromS0"></a><a id="wdfdevstatepwrpolwokefroms0"></a><a id="WDFDEVSTATEPWRPOLWOKEFROMS0"></a><b>WdfDevStatePwrPolWokeFromS0</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWokeFromS0NotifyDriver"></a><a id="wdfdevstatepwrpolwokefroms0notifydriver"></a><a id="WDFDEVSTATEPWRPOLWOKEFROMS0NOTIFYDRIVER"></a><b>WdfDevStatePwrPolWokeFromS0NotifyDriver</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingResetDevice"></a><a id="wdfdevstatepwrpolstoppingresetdevice"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGRESETDEVICE"></a><b>WdfDevStatePwrPolStoppingResetDevice</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingResetDeviceCompletePowerUp"></a><a id="wdfdevstatepwrpolstoppingresetdevicecompletepowerup"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGRESETDEVICECOMPLETEPOWERUP"></a><b>WdfDevStatePwrPolStoppingResetDeviceCompletePowerUp</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingResetDeviceFailed"></a><a id="wdfdevstatepwrpolstoppingresetdevicefailed"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGRESETDEVICEFAILED"></a><b>WdfDevStatePwrPolStoppingResetDeviceFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingD0"></a><a id="wdfdevstatepwrpolstoppingd0"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGD0"></a><b>WdfDevStatePwrPolStoppingD0</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingD0Failed"></a><a id="wdfdevstatepwrpolstoppingd0failed"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGD0FAILED"></a><b>WdfDevStatePwrPolStoppingD0Failed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingDisarmWake"></a><a id="wdfdevstatepwrpolstoppingdisarmwake"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGDISARMWAKE"></a><b>WdfDevStatePwrPolStoppingDisarmWake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingDisarmWakeCancelWake"></a><a id="wdfdevstatepwrpolstoppingdisarmwakecancelwake"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGDISARMWAKECANCELWAKE"></a><b>WdfDevStatePwrPolStoppingDisarmWakeCancelWake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingDisarmWakeWakeCanceled"></a><a id="wdfdevstatepwrpolstoppingdisarmwakewakecanceled"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGDISARMWAKEWAKECANCELED"></a><b>WdfDevStatePwrPolStoppingDisarmWakeWakeCanceled</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStopping"></a><a id="wdfdevstatepwrpolstopping"></a><a id="WDFDEVSTATEPWRPOLSTOPPING"></a><b>WdfDevStatePwrPolStopping</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingFailed"></a><a id="wdfdevstatepwrpolstoppingfailed"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGFAILED"></a><b>WdfDevStatePwrPolStoppingFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingSendStatus"></a><a id="wdfdevstatepwrpolstoppingsendstatus"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGSENDSTATUS"></a><b>WdfDevStatePwrPolStoppingSendStatus</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingCancelTimer"></a><a id="wdfdevstatepwrpolstoppingcanceltimer"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGCANCELTIMER"></a><b>WdfDevStatePwrPolStoppingCancelTimer</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingWaitForIdleTimeout"></a><a id="wdfdevstatepwrpolstoppingwaitforidletimeout"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGWAITFORIDLETIMEOUT"></a><b>WdfDevStatePwrPolStoppingWaitForIdleTimeout</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingCancelUsbSS"></a><a id="wdfdevstatepwrpolstoppingcancelusbss"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGCANCELUSBSS"></a><b>WdfDevStatePwrPolStoppingCancelUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingWaitForUsbSSCompletion"></a><a id="wdfdevstatepwrpolstoppingwaitforusbsscompletion"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGWAITFORUSBSSCOMPLETION"></a><b>WdfDevStatePwrPolStoppingWaitForUsbSSCompletion</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingCancelWake"></a><a id="wdfdevstatepwrpolstoppingcancelwake"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGCANCELWAKE"></a><b>WdfDevStatePwrPolStoppingCancelWake</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStopped"></a><a id="wdfdevstatepwrpolstopped"></a><a id="WDFDEVSTATEPWRPOLSTOPPED"></a><b>WdfDevStatePwrPolStopped</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolCancelUsbSS"></a><a id="wdfdevstatepwrpolcancelusbss"></a><a id="WDFDEVSTATEPWRPOLCANCELUSBSS"></a><b>WdfDevStatePwrPolCancelUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStarted"></a><a id="wdfdevstatepwrpolstarted"></a><a id="WDFDEVSTATEPWRPOLSTARTED"></a><b>WdfDevStatePwrPolStarted</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartedCancelTimer"></a><a id="wdfdevstatepwrpolstartedcanceltimer"></a><a id="WDFDEVSTATEPWRPOLSTARTEDCANCELTIMER"></a><b>WdfDevStatePwrPolStartedCancelTimer</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartedWaitForIdleTimeout"></a><a id="wdfdevstatepwrpolstartedwaitforidletimeout"></a><a id="WDFDEVSTATEPWRPOLSTARTEDWAITFORIDLETIMEOUT"></a><b>WdfDevStatePwrPolStartedWaitForIdleTimeout</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartedWakeCapableCancelTimerForSleep"></a><a id="wdfdevstatepwrpolstartedwakecapablecanceltimerforsleep"></a><a id="WDFDEVSTATEPWRPOLSTARTEDWAKECAPABLECANCELTIMERFORSLEEP"></a><b>WdfDevStatePwrPolStartedWakeCapableCancelTimerForSleep</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartedWakeCapableWaitForIdleTimeout"></a><a id="wdfdevstatepwrpolstartedwakecapablewaitforidletimeout"></a><a id="WDFDEVSTATEPWRPOLSTARTEDWAKECAPABLEWAITFORIDLETIMEOUT"></a><b>WdfDevStatePwrPolStartedWakeCapableWaitForIdleTimeout</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartedWakeCapableSleepingUsbSS"></a><a id="wdfdevstatepwrpolstartedwakecapablesleepingusbss"></a><a id="WDFDEVSTATEPWRPOLSTARTEDWAKECAPABLESLEEPINGUSBSS"></a><b>WdfDevStatePwrPolStartedWakeCapableSleepingUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartedIdleCapableCancelTimerForSleep"></a><a id="wdfdevstatepwrpolstartedidlecapablecanceltimerforsleep"></a><a id="WDFDEVSTATEPWRPOLSTARTEDIDLECAPABLECANCELTIMERFORSLEEP"></a><b>WdfDevStatePwrPolStartedIdleCapableCancelTimerForSleep</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartedIdleCapableWaitForIdleTimeout"></a><a id="wdfdevstatepwrpolstartedidlecapablewaitforidletimeout"></a><a id="WDFDEVSTATEPWRPOLSTARTEDIDLECAPABLEWAITFORIDLETIMEOUT"></a><b>WdfDevStatePwrPolStartedIdleCapableWaitForIdleTimeout</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolDeviceD0PowerRequestFailed"></a><a id="wdfdevstatepwrpoldeviced0powerrequestfailed"></a><a id="WDFDEVSTATEPWRPOLDEVICED0POWERREQUESTFAILED"></a><b>WdfDevStatePwrPolDeviceD0PowerRequestFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolDevicePowerRequestFailed"></a><a id="wdfdevstatepwrpoldevicepowerrequestfailed"></a><a id="WDFDEVSTATEPWRPOLDEVICEPOWERREQUESTFAILED"></a><b>WdfDevStatePwrPolDevicePowerRequestFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolGotoDx"></a><a id="wdfdevstatepwrpolgotodx"></a><a id="WDFDEVSTATEPWRPOLGOTODX"></a><b>WdfDevStatePwrPolGotoDx</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolGotoDxInDx"></a><a id="wdfdevstatepwrpolgotodxindx"></a><a id="WDFDEVSTATEPWRPOLGOTODXINDX"></a><b>WdfDevStatePwrPolGotoDxInDx</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolDx"></a><a id="wdfdevstatepwrpoldx"></a><a id="WDFDEVSTATEPWRPOLDX"></a><b>WdfDevStatePwrPolDx</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolGotoD0"></a><a id="wdfdevstatepwrpolgotod0"></a><a id="WDFDEVSTATEPWRPOLGOTOD0"></a><b>WdfDevStatePwrPolGotoD0</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolGotoD0InD0"></a><a id="wdfdevstatepwrpolgotod0ind0"></a><a id="WDFDEVSTATEPWRPOLGOTOD0IND0"></a><b>WdfDevStatePwrPolGotoD0InD0</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolFinal"></a><a id="wdfdevstatepwrpolfinal"></a><a id="WDFDEVSTATEPWRPOLFINAL"></a><b>WdfDevStatePwrPolFinal</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSleepingPowerDownNotProcessed"></a><a id="wdfdevstatepwrpolsleepingpowerdownnotprocessed"></a><a id="WDFDEVSTATEPWRPOLSLEEPINGPOWERDOWNNOTPROCESSED"></a><b>WdfDevStatePwrPolSleepingPowerDownNotProcessed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownNotProcessed"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablepowerdownnotprocessed"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEPOWERDOWNNOTPROCESSED"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownNotProcessed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredNoWakePowerDownNotProcessed"></a><a id="wdfdevstatepwrpoltimerexpirednowakepowerdownnotprocessed"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDNOWAKEPOWERDOWNNOTPROCESSED"></a><b>WdfDevStatePwrPolTimerExpiredNoWakePowerDownNotProcessed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredNoWakePoweredDownDisableIdleTimer"></a><a id="wdfdevstatepwrpoltimerexpirednowakepowereddowndisableidletimer"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDNOWAKEPOWEREDDOWNDISABLEIDLETIMER"></a><b>WdfDevStatePwrPolTimerExpiredNoWakePoweredDownDisableIdleTimer</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingWaitingForImplicitPowerDown"></a><a id="wdfdevstatepwrpolstoppingwaitingforimplicitpowerdown"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGWAITINGFORIMPLICITPOWERDOWN"></a><b>WdfDevStatePwrPolStoppingWaitingForImplicitPowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingPoweringUp"></a><a id="wdfdevstatepwrpolstoppingpoweringup"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGPOWERINGUP"></a><b>WdfDevStatePwrPolStoppingPoweringUp</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingPoweringDown"></a><a id="wdfdevstatepwrpolstoppingpoweringdown"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGPOWERINGDOWN"></a><b>WdfDevStatePwrPolStoppingPoweringDown</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolPowerUpForSystemSleepNotSeen"></a><a id="wdfdevstatepwrpolpowerupforsystemsleepnotseen"></a><a id="WDFDEVSTATEPWRPOLPOWERUPFORSYSTEMSLEEPNOTSEEN"></a><b>WdfDevStatePwrPolPowerUpForSystemSleepNotSeen</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWaitingArmedStoppingCancelUsbSS"></a><a id="wdfdevstatepwrpolwaitingarmedstoppingcancelusbss"></a><a id="WDFDEVSTATEPWRPOLWAITINGARMEDSTOPPINGCANCELUSBSS"></a><b>WdfDevStatePwrPolWaitingArmedStoppingCancelUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWaitingArmedWakeFailedCancelUsbSS"></a><a id="wdfdevstatepwrpolwaitingarmedwakefailedcancelusbss"></a><a id="WDFDEVSTATEPWRPOLWAITINGARMEDWAKEFAILEDCANCELUSBSS"></a><b>WdfDevStatePwrPolWaitingArmedWakeFailedCancelUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWaitingArmedIoPresentCancelUsbSS"></a><a id="wdfdevstatepwrpolwaitingarmediopresentcancelusbss"></a><a id="WDFDEVSTATEPWRPOLWAITINGARMEDIOPRESENTCANCELUSBSS"></a><b>WdfDevStatePwrPolWaitingArmedIoPresentCancelUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWaitingArmedWakeSucceededCancelUsbSS"></a><a id="wdfdevstatepwrpolwaitingarmedwakesucceededcancelusbss"></a><a id="WDFDEVSTATEPWRPOLWAITINGARMEDWAKESUCCEEDEDCANCELUSBSS"></a><b>WdfDevStatePwrPolWaitingArmedWakeSucceededCancelUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolCancelingUsbSSForSystemSleep"></a><a id="wdfdevstatepwrpolcancelingusbssforsystemsleep"></a><a id="WDFDEVSTATEPWRPOLCANCELINGUSBSSFORSYSTEMSLEEP"></a><b>WdfDevStatePwrPolCancelingUsbSSForSystemSleep</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppingD0CancelUsbSS"></a><a id="wdfdevstatepwrpolstoppingd0cancelusbss"></a><a id="WDFDEVSTATEPWRPOLSTOPPINGD0CANCELUSBSS"></a><b>WdfDevStatePwrPolStoppingD0CancelUsbSS</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartingPoweredUp"></a><a id="wdfdevstatepwrpolstartingpoweredup"></a><a id="WDFDEVSTATEPWRPOLSTARTINGPOWEREDUP"></a><b>WdfDevStatePwrPolStartingPoweredUp</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolIdleCapableDeviceIdle"></a><a id="wdfdevstatepwrpolidlecapabledeviceidle"></a><a id="WDFDEVSTATEPWRPOLIDLECAPABLEDEVICEIDLE"></a><b>WdfDevStatePwrPolIdleCapableDeviceIdle</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolDeviceIdleReturnToActive"></a><a id="wdfdevstatepwrpoldeviceidlereturntoactive"></a><a id="WDFDEVSTATEPWRPOLDEVICEIDLERETURNTOACTIVE"></a><b>WdfDevStatePwrPolDeviceIdleReturnToActive</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolDeviceIdleSleeping"></a><a id="wdfdevstatepwrpoldeviceidlesleeping"></a><a id="WDFDEVSTATEPWRPOLDEVICEIDLESLEEPING"></a><b>WdfDevStatePwrPolDeviceIdleSleeping</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolDeviceIdleStopping"></a><a id="wdfdevstatepwrpoldeviceidlestopping"></a><a id="WDFDEVSTATEPWRPOLDEVICEIDLESTOPPING"></a><b>WdfDevStatePwrPolDeviceIdleStopping</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredNoWakeUndoPowerDown"></a><a id="wdfdevstatepwrpoltimerexpirednowakeundopowerdown"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDNOWAKEUNDOPOWERDOWN"></a><b>WdfDevStatePwrPolTimerExpiredNoWakeUndoPowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWakeCapableDeviceIdle"></a><a id="wdfdevstatepwrpolwakecapabledeviceidle"></a><a id="WDFDEVSTATEPWRPOLWAKECAPABLEDEVICEIDLE"></a><b>WdfDevStatePwrPolWakeCapableDeviceIdle</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWakeCapableUsbSSCompleted"></a><a id="wdfdevstatepwrpolwakecapableusbsscompleted"></a><a id="WDFDEVSTATEPWRPOLWAKECAPABLEUSBSSCOMPLETED"></a><b>WdfDevStatePwrPolWakeCapableUsbSSCompleted</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapableUndoPowerDown"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapableundopowerdown"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEUNDOPOWERDOWN"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapableUndoPowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCompletedHardwareStarted"></a><a id="wdfdevstatepwrpoltimerexpiredwakecompletedhardwarestarted"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECOMPLETEDHARDWARESTARTED"></a><b>WdfDevStatePwrPolTimerExpiredWakeCompletedHardwareStarted</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStoppedRemoving"></a><a id="wdfdevstatepwrpolstoppedremoving"></a><a id="WDFDEVSTATEPWRPOLSTOPPEDREMOVING"></a><b>WdfDevStatePwrPolStoppedRemoving</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolRemoved"></a><a id="wdfdevstatepwrpolremoved"></a><a id="WDFDEVSTATEPWRPOLREMOVED"></a><b>WdfDevStatePwrPolRemoved</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolRestarting"></a><a id="wdfdevstatepwrpolrestarting"></a><a id="WDFDEVSTATEPWRPOLRESTARTING"></a><b>WdfDevStatePwrPolRestarting</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolRestartingFailed"></a><a id="wdfdevstatepwrpolrestartingfailed"></a><a id="WDFDEVSTATEPWRPOLRESTARTINGFAILED"></a><b>WdfDevStatePwrPolRestartingFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolStartingPoweredUpFailed"></a><a id="wdfdevstatepwrpolstartingpoweredupfailed"></a><a id="WDFDEVSTATEPWRPOLSTARTINGPOWEREDUPFAILED"></a><b>WdfDevStatePwrPolStartingPoweredUpFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredNoWakeReturnToActive"></a><a id="wdfdevstatepwrpoltimerexpirednowakereturntoactive"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDNOWAKERETURNTOACTIVE"></a><b>WdfDevStatePwrPolTimerExpiredNoWakeReturnToActive</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWaitingArmedWakeInterruptFired"></a><a id="wdfdevstatepwrpolwaitingarmedwakeinterruptfired"></a><a id="WDFDEVSTATEPWRPOLWAITINGARMEDWAKEINTERRUPTFIRED"></a><b>WdfDevStatePwrPolWaitingArmedWakeInterruptFired</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFired"></a><a id="wdfdevstatepwrpolsystemwakedevicewakeinterruptfired"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKEINTERRUPTFIRED"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFired</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFiredNP"></a><a id="wdfdevstatepwrpolsystemwakedevicewakeinterruptfirednp"></a><a id="WDFDEVSTATEPWRPOLSYSTEMWAKEDEVICEWAKEINTERRUPTFIREDNP"></a><b>WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFiredNP</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapableWakeInterruptArrived"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablewakeinterruptarrived"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEWAKEINTERRUPTARRIVED"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapableWakeInterruptArrived</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeInterruptArrived"></a><a id="wdfdevstatepwrpoltimerexpiredwakecapablepowerdownfailedwakeinterruptarrived"></a><a id="WDFDEVSTATEPWRPOLTIMEREXPIREDWAKECAPABLEPOWERDOWNFAILEDWAKEINTERRUPTARRIVED"></a><b>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeInterruptArrived</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolWaitingArmedWakeInterruptFiredDuringPowerDown"></a><a id="wdfdevstatepwrpolwaitingarmedwakeinterruptfiredduringpowerdown"></a><a id="WDFDEVSTATEPWRPOLWAITINGARMEDWAKEINTERRUPTFIREDDURINGPOWERDOWN"></a><b>WdfDevStatePwrPolWaitingArmedWakeInterruptFiredDuringPowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePwrPolNull"></a><a id="wdfdevstatepwrpolnull"></a><a id="WDFDEVSTATEPWRPOLNULL"></a><b>WdfDevStatePwrPolNull</b>

<dd></dd>
</dl>

## -remarks
<p>The WDF_DEVICE_POWER_POLICY_STATE enumeration is used as a member type in the <a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-notification-data.md">WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA</a> structure and as the return type for the <a href="..\wdfdevice\nf-wdfdevice-wdfdevicegetdevicepowerpolicystate.md">WdfDeviceGetDevicePowerPolicyState</a> method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>