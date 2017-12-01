---
UID: NE.wdfdevice._WDF_DEVICE_POWER_STATE
title: WDF_DEVICE_POWER_STATE
author: windows-driver-content
description: The WDF_DEVICE_POWER_STATE enumeration identifies all of the states that the framework's power state machine can enter.
old-location: wdf\wdf_device_power_state.htm
old-project: wdf
ms.assetid: 06bb6465-afc6-4b92-b3d7-1c66f6c6c33d
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
req.alt-api: WDF_DEVICE_POWER_STATE
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

# WDF_DEVICE_POWER_STATE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_DEVICE_POWER_STATE</b> enumeration identifies all of the states that the framework's power state machine can enter.</p>


## -syntax

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


## -enum-fields
<dl>

### -field <a id="WdfDevStatePowerInvalid"></a><a id="wdfdevstatepowerinvalid"></a><a id="WDFDEVSTATEPOWERINVALID"></a><b>WdfDevStatePowerInvalid</b>

<dd></dd>

### -field <a id="WdfDevStatePowerObjectCreated"></a><a id="wdfdevstatepowerobjectcreated"></a><a id="WDFDEVSTATEPOWEROBJECTCREATED"></a><b>WdfDevStatePowerObjectCreated</b>

<dd></dd>

### -field <a id="WdfDevStatePowerCheckDeviceType"></a><a id="wdfdevstatepowercheckdevicetype"></a><a id="WDFDEVSTATEPOWERCHECKDEVICETYPE"></a><b>WdfDevStatePowerCheckDeviceType</b>

<dd></dd>

### -field <a id="WdfDevStatePowerCheckDeviceTypeNP"></a><a id="wdfdevstatepowercheckdevicetypenp"></a><a id="WDFDEVSTATEPOWERCHECKDEVICETYPENP"></a><b>WdfDevStatePowerCheckDeviceTypeNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerCheckParentState"></a><a id="wdfdevstatepowercheckparentstate"></a><a id="WDFDEVSTATEPOWERCHECKPARENTSTATE"></a><b>WdfDevStatePowerCheckParentState</b>

<dd></dd>

### -field <a id="WdfDevStatePowerCheckParentStateNP"></a><a id="wdfdevstatepowercheckparentstatenp"></a><a id="WDFDEVSTATEPOWERCHECKPARENTSTATENP"></a><b>WdfDevStatePowerCheckParentStateNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerEnablingWakeAtBus"></a><a id="wdfdevstatepowerenablingwakeatbus"></a><a id="WDFDEVSTATEPOWERENABLINGWAKEATBUS"></a><b>WdfDevStatePowerEnablingWakeAtBus</b>

<dd></dd>

### -field <a id="WdfDevStatePowerEnablingWakeAtBusNP"></a><a id="wdfdevstatepowerenablingwakeatbusnp"></a><a id="WDFDEVSTATEPOWERENABLINGWAKEATBUSNP"></a><b>WdfDevStatePowerEnablingWakeAtBusNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0"></a><a id="wdfdevstatepowerd0"></a><a id="WDFDEVSTATEPOWERD0"></a><b>WdfDevStatePowerD0</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0NP"></a><a id="wdfdevstatepowerd0np"></a><a id="WDFDEVSTATEPOWERD0NP"></a><b>WdfDevStatePowerD0NP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0BusWakeOwner"></a><a id="wdfdevstatepowerd0buswakeowner"></a><a id="WDFDEVSTATEPOWERD0BUSWAKEOWNER"></a><b>WdfDevStatePowerD0BusWakeOwner</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0BusWakeOwnerNP"></a><a id="wdfdevstatepowerd0buswakeownernp"></a><a id="WDFDEVSTATEPOWERD0BUSWAKEOWNERNP"></a><b>WdfDevStatePowerD0BusWakeOwnerNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0ArmedForWake"></a><a id="wdfdevstatepowerd0armedforwake"></a><a id="WDFDEVSTATEPOWERD0ARMEDFORWAKE"></a><b>WdfDevStatePowerD0ArmedForWake</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0ArmedForWakeNP"></a><a id="wdfdevstatepowerd0armedforwakenp"></a><a id="WDFDEVSTATEPOWERD0ARMEDFORWAKENP"></a><b>WdfDevStatePowerD0ArmedForWakeNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0DisarmingWakeAtBus"></a><a id="wdfdevstatepowerd0disarmingwakeatbus"></a><a id="WDFDEVSTATEPOWERD0DISARMINGWAKEATBUS"></a><b>WdfDevStatePowerD0DisarmingWakeAtBus</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0DisarmingWakeAtBusNP"></a><a id="wdfdevstatepowerd0disarmingwakeatbusnp"></a><a id="WDFDEVSTATEPOWERD0DISARMINGWAKEATBUSNP"></a><b>WdfDevStatePowerD0DisarmingWakeAtBusNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0Starting"></a><a id="wdfdevstatepowerd0starting"></a><a id="WDFDEVSTATEPOWERD0STARTING"></a><b>WdfDevStatePowerD0Starting</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0StartingConnectInterrupt"></a><a id="wdfdevstatepowerd0startingconnectinterrupt"></a><a id="WDFDEVSTATEPOWERD0STARTINGCONNECTINTERRUPT"></a><b>WdfDevStatePowerD0StartingConnectInterrupt</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0StartingDmaEnable"></a><a id="wdfdevstatepowerd0startingdmaenable"></a><a id="WDFDEVSTATEPOWERD0STARTINGDMAENABLE"></a><b>WdfDevStatePowerD0StartingDmaEnable</b>

<dd></dd>

### -field <a id="WdfDevStatePowerD0StartingStartSelfManagedIo"></a><a id="wdfdevstatepowerd0startingstartselfmanagedio"></a><a id="WDFDEVSTATEPOWERD0STARTINGSTARTSELFMANAGEDIO"></a><b>WdfDevStatePowerD0StartingStartSelfManagedIo</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDecideD0State"></a><a id="wdfdevstatepowerdecided0state"></a><a id="WDFDEVSTATEPOWERDECIDED0STATE"></a><b>WdfDevStatePowerDecideD0State</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoD3Stopped"></a><a id="wdfdevstatepowergotod3stopped"></a><a id="WDFDEVSTATEPOWERGOTOD3STOPPED"></a><b>WdfDevStatePowerGotoD3Stopped</b>

<dd></dd>

### -field <a id="WdfDevStatePowerStopped"></a><a id="wdfdevstatepowerstopped"></a><a id="WDFDEVSTATEPOWERSTOPPED"></a><b>WdfDevStatePowerStopped</b>

<dd></dd>

### -field <a id="WdfDevStatePowerStartingCheckDeviceType"></a><a id="wdfdevstatepowerstartingcheckdevicetype"></a><a id="WDFDEVSTATEPOWERSTARTINGCHECKDEVICETYPE"></a><b>WdfDevStatePowerStartingCheckDeviceType</b>

<dd></dd>

### -field <a id="WdfDevStatePowerStartingChild"></a><a id="wdfdevstatepowerstartingchild"></a><a id="WDFDEVSTATEPOWERSTARTINGCHILD"></a><b>WdfDevStatePowerStartingChild</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDxDisablingWakeAtBus"></a><a id="wdfdevstatepowerdxdisablingwakeatbus"></a><a id="WDFDEVSTATEPOWERDXDISABLINGWAKEATBUS"></a><b>WdfDevStatePowerDxDisablingWakeAtBus</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDxDisablingWakeAtBusNP"></a><a id="wdfdevstatepowerdxdisablingwakeatbusnp"></a><a id="WDFDEVSTATEPOWERDXDISABLINGWAKEATBUSNP"></a><b>WdfDevStatePowerDxDisablingWakeAtBusNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDx"></a><a id="wdfdevstatepowergotodx"></a><a id="WDFDEVSTATEPOWERGOTODX"></a><b>WdfDevStatePowerGotoDx</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxNP"></a><a id="wdfdevstatepowergotodxnp"></a><a id="WDFDEVSTATEPOWERGOTODXNP"></a><b>WdfDevStatePowerGotoDxNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxIoStopped"></a><a id="wdfdevstatepowergotodxiostopped"></a><a id="WDFDEVSTATEPOWERGOTODXIOSTOPPED"></a><b>WdfDevStatePowerGotoDxIoStopped</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxIoStoppedNP"></a><a id="wdfdevstatepowergotodxiostoppednp"></a><a id="WDFDEVSTATEPOWERGOTODXIOSTOPPEDNP"></a><b>WdfDevStatePowerGotoDxIoStoppedNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxNPFailed"></a><a id="wdfdevstatepowergotodxnpfailed"></a><a id="WDFDEVSTATEPOWERGOTODXNPFAILED"></a><b>WdfDevStatePowerGotoDxNPFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDx"></a><a id="wdfdevstatepowerdx"></a><a id="WDFDEVSTATEPOWERDX"></a><b>WdfDevStatePowerDx</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDxNP"></a><a id="wdfdevstatepowerdxnp"></a><a id="WDFDEVSTATEPOWERDXNP"></a><b>WdfDevStatePowerDxNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxArmedForWake"></a><a id="wdfdevstatepowergotodxarmedforwake"></a><a id="WDFDEVSTATEPOWERGOTODXARMEDFORWAKE"></a><b>WdfDevStatePowerGotoDxArmedForWake</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxArmedForWakeNP"></a><a id="wdfdevstatepowergotodxarmedforwakenp"></a><a id="WDFDEVSTATEPOWERGOTODXARMEDFORWAKENP"></a><b>WdfDevStatePowerGotoDxArmedForWakeNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxIoStoppedArmedForWake"></a><a id="wdfdevstatepowergotodxiostoppedarmedforwake"></a><a id="WDFDEVSTATEPOWERGOTODXIOSTOPPEDARMEDFORWAKE"></a><b>WdfDevStatePowerGotoDxIoStoppedArmedForWake</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxIoStoppedArmedForWakeNP"></a><a id="wdfdevstatepowergotodxiostoppedarmedforwakenp"></a><a id="WDFDEVSTATEPOWERGOTODXIOSTOPPEDARMEDFORWAKENP"></a><b>WdfDevStatePowerGotoDxIoStoppedArmedForWakeNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDxArmedForWake"></a><a id="wdfdevstatepowerdxarmedforwake"></a><a id="WDFDEVSTATEPOWERDXARMEDFORWAKE"></a><b>WdfDevStatePowerDxArmedForWake</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDxArmedForWakeNP"></a><a id="wdfdevstatepowerdxarmedforwakenp"></a><a id="WDFDEVSTATEPOWERDXARMEDFORWAKENP"></a><b>WdfDevStatePowerDxArmedForWakeNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerCheckParentStateArmedForWake"></a><a id="wdfdevstatepowercheckparentstatearmedforwake"></a><a id="WDFDEVSTATEPOWERCHECKPARENTSTATEARMEDFORWAKE"></a><b>WdfDevStatePowerCheckParentStateArmedForWake</b>

<dd></dd>

### -field <a id="WdfDevStatePowerCheckParentStateArmedForWakeNP"></a><a id="wdfdevstatepowercheckparentstatearmedforwakenp"></a><a id="WDFDEVSTATEPOWERCHECKPARENTSTATEARMEDFORWAKENP"></a><b>WdfDevStatePowerCheckParentStateArmedForWakeNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWaitForParentArmedForWake"></a><a id="wdfdevstatepowerwaitforparentarmedforwake"></a><a id="WDFDEVSTATEPOWERWAITFORPARENTARMEDFORWAKE"></a><b>WdfDevStatePowerWaitForParentArmedForWake</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWaitForParentArmedForWakeNP"></a><a id="wdfdevstatepowerwaitforparentarmedforwakenp"></a><a id="WDFDEVSTATEPOWERWAITFORPARENTARMEDFORWAKENP"></a><b>WdfDevStatePowerWaitForParentArmedForWakeNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerStartSelfManagedIo"></a><a id="wdfdevstatepowerstartselfmanagedio"></a><a id="WDFDEVSTATEPOWERSTARTSELFMANAGEDIO"></a><b>WdfDevStatePowerStartSelfManagedIo</b>

<dd></dd>

### -field <a id="WdfDevStatePowerStartSelfManagedIoNP"></a><a id="wdfdevstatepowerstartselfmanagedionp"></a><a id="WDFDEVSTATEPOWERSTARTSELFMANAGEDIONP"></a><b>WdfDevStatePowerStartSelfManagedIoNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerStartSelfManagedIoFailed"></a><a id="wdfdevstatepowerstartselfmanagediofailed"></a><a id="WDFDEVSTATEPOWERSTARTSELFMANAGEDIOFAILED"></a><b>WdfDevStatePowerStartSelfManagedIoFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerStartSelfManagedIoFailedNP"></a><a id="wdfdevstatepowerstartselfmanagediofailednp"></a><a id="WDFDEVSTATEPOWERSTARTSELFMANAGEDIOFAILEDNP"></a><b>WdfDevStatePowerStartSelfManagedIoFailedNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWaitForParent"></a><a id="wdfdevstatepowerwaitforparent"></a><a id="WDFDEVSTATEPOWERWAITFORPARENT"></a><b>WdfDevStatePowerWaitForParent</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWaitForParentNP"></a><a id="wdfdevstatepowerwaitforparentnp"></a><a id="WDFDEVSTATEPOWERWAITFORPARENTNP"></a><b>WdfDevStatePowerWaitForParentNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWakePending"></a><a id="wdfdevstatepowerwakepending"></a><a id="WDFDEVSTATEPOWERWAKEPENDING"></a><b>WdfDevStatePowerWakePending</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWakePendingNP"></a><a id="wdfdevstatepowerwakependingnp"></a><a id="WDFDEVSTATEPOWERWAKEPENDINGNP"></a><b>WdfDevStatePowerWakePendingNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWaking"></a><a id="wdfdevstatepowerwaking"></a><a id="WDFDEVSTATEPOWERWAKING"></a><b>WdfDevStatePowerWaking</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWakingNP"></a><a id="wdfdevstatepowerwakingnp"></a><a id="WDFDEVSTATEPOWERWAKINGNP"></a><b>WdfDevStatePowerWakingNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWakingConnectInterrupt"></a><a id="wdfdevstatepowerwakingconnectinterrupt"></a><a id="WDFDEVSTATEPOWERWAKINGCONNECTINTERRUPT"></a><b>WdfDevStatePowerWakingConnectInterrupt</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWakingConnectInterruptNP"></a><a id="wdfdevstatepowerwakingconnectinterruptnp"></a><a id="WDFDEVSTATEPOWERWAKINGCONNECTINTERRUPTNP"></a><b>WdfDevStatePowerWakingConnectInterruptNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWakingConnectInterruptFailed"></a><a id="wdfdevstatepowerwakingconnectinterruptfailed"></a><a id="WDFDEVSTATEPOWERWAKINGCONNECTINTERRUPTFAILED"></a><b>WdfDevStatePowerWakingConnectInterruptFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWakingConnectInterruptFailedNP"></a><a id="wdfdevstatepowerwakingconnectinterruptfailednp"></a><a id="WDFDEVSTATEPOWERWAKINGCONNECTINTERRUPTFAILEDNP"></a><b>WdfDevStatePowerWakingConnectInterruptFailedNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWakingDmaEnable"></a><a id="wdfdevstatepowerwakingdmaenable"></a><a id="WDFDEVSTATEPOWERWAKINGDMAENABLE"></a><b>WdfDevStatePowerWakingDmaEnable</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWakingDmaEnableNP"></a><a id="wdfdevstatepowerwakingdmaenablenp"></a><a id="WDFDEVSTATEPOWERWAKINGDMAENABLENP"></a><b>WdfDevStatePowerWakingDmaEnableNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWakingDmaEnableFailed"></a><a id="wdfdevstatepowerwakingdmaenablefailed"></a><a id="WDFDEVSTATEPOWERWAKINGDMAENABLEFAILED"></a><b>WdfDevStatePowerWakingDmaEnableFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerWakingDmaEnableFailedNP"></a><a id="wdfdevstatepowerwakingdmaenablefailednp"></a><a id="WDFDEVSTATEPOWERWAKINGDMAENABLEFAILEDNP"></a><b>WdfDevStatePowerWakingDmaEnableFailedNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerReportPowerUpFailedDerefParent"></a><a id="wdfdevstatepowerreportpowerupfailedderefparent"></a><a id="WDFDEVSTATEPOWERREPORTPOWERUPFAILEDDEREFPARENT"></a><b>WdfDevStatePowerReportPowerUpFailedDerefParent</b>

<dd></dd>

### -field <a id="WdfDevStatePowerReportPowerUpFailed"></a><a id="wdfdevstatepowerreportpowerupfailed"></a><a id="WDFDEVSTATEPOWERREPORTPOWERUPFAILED"></a><b>WdfDevStatePowerReportPowerUpFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerPowerFailedPowerDown"></a><a id="wdfdevstatepowerpowerfailedpowerdown"></a><a id="WDFDEVSTATEPOWERPOWERFAILEDPOWERDOWN"></a><b>WdfDevStatePowerPowerFailedPowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePowerReportPowerDownFailed"></a><a id="wdfdevstatepowerreportpowerdownfailed"></a><a id="WDFDEVSTATEPOWERREPORTPOWERDOWNFAILED"></a><b>WdfDevStatePowerReportPowerDownFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerInitialConnectInterruptFailed"></a><a id="wdfdevstatepowerinitialconnectinterruptfailed"></a><a id="WDFDEVSTATEPOWERINITIALCONNECTINTERRUPTFAILED"></a><b>WdfDevStatePowerInitialConnectInterruptFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerInitialDmaEnableFailed"></a><a id="wdfdevstatepowerinitialdmaenablefailed"></a><a id="WDFDEVSTATEPOWERINITIALDMAENABLEFAILED"></a><b>WdfDevStatePowerInitialDmaEnableFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerInitialSelfManagedIoFailed"></a><a id="wdfdevstatepowerinitialselfmanagediofailed"></a><a id="WDFDEVSTATEPOWERINITIALSELFMANAGEDIOFAILED"></a><b>WdfDevStatePowerInitialSelfManagedIoFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerInitialPowerUpFailedDerefParent"></a><a id="wdfdevstatepowerinitialpowerupfailedderefparent"></a><a id="WDFDEVSTATEPOWERINITIALPOWERUPFAILEDDEREFPARENT"></a><b>WdfDevStatePowerInitialPowerUpFailedDerefParent</b>

<dd></dd>

### -field <a id="WdfDevStatePowerInitialPowerUpFailed"></a><a id="wdfdevstatepowerinitialpowerupfailed"></a><a id="WDFDEVSTATEPOWERINITIALPOWERUPFAILED"></a><b>WdfDevStatePowerInitialPowerUpFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDxStoppedDisarmWake"></a><a id="wdfdevstatepowerdxstoppeddisarmwake"></a><a id="WDFDEVSTATEPOWERDXSTOPPEDDISARMWAKE"></a><b>WdfDevStatePowerDxStoppedDisarmWake</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDxStoppedDisarmWakeNP"></a><a id="wdfdevstatepowerdxstoppeddisarmwakenp"></a><a id="WDFDEVSTATEPOWERDXSTOPPEDDISARMWAKENP"></a><b>WdfDevStatePowerDxStoppedDisarmWakeNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxStoppedDisableInterruptNP"></a><a id="wdfdevstatepowergotodxstoppeddisableinterruptnp"></a><a id="WDFDEVSTATEPOWERGOTODXSTOPPEDDISABLEINTERRUPTNP"></a><b>WdfDevStatePowerGotoDxStoppedDisableInterruptNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxStopped"></a><a id="wdfdevstatepowergotodxstopped"></a><a id="WDFDEVSTATEPOWERGOTODXSTOPPED"></a><b>WdfDevStatePowerGotoDxStopped</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDxStopped"></a><a id="wdfdevstatepowerdxstopped"></a><a id="WDFDEVSTATEPOWERDXSTOPPED"></a><b>WdfDevStatePowerDxStopped</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoStopped"></a><a id="wdfdevstatepowergotostopped"></a><a id="WDFDEVSTATEPOWERGOTOSTOPPED"></a><b>WdfDevStatePowerGotoStopped</b>

<dd></dd>

### -field <a id="WdfDevStatePowerStoppedCompleteDx"></a><a id="wdfdevstatepowerstoppedcompletedx"></a><a id="WDFDEVSTATEPOWERSTOPPEDCOMPLETEDX"></a><b>WdfDevStatePowerStoppedCompleteDx</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDxStoppedDecideDxState"></a><a id="wdfdevstatepowerdxstoppeddecidedxstate"></a><a id="WDFDEVSTATEPOWERDXSTOPPEDDECIDEDXSTATE"></a><b>WdfDevStatePowerDxStoppedDecideDxState</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDxStoppedArmForWake"></a><a id="wdfdevstatepowerdxstoppedarmforwake"></a><a id="WDFDEVSTATEPOWERDXSTOPPEDARMFORWAKE"></a><b>WdfDevStatePowerDxStoppedArmForWake</b>

<dd></dd>

### -field <a id="WdfDevStatePowerDxStoppedArmForWakeNP"></a><a id="wdfdevstatepowerdxstoppedarmforwakenp"></a><a id="WDFDEVSTATEPOWERDXSTOPPEDARMFORWAKENP"></a><b>WdfDevStatePowerDxStoppedArmForWakeNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerFinalPowerDownFailed"></a><a id="wdfdevstatepowerfinalpowerdownfailed"></a><a id="WDFDEVSTATEPOWERFINALPOWERDOWNFAILED"></a><b>WdfDevStatePowerFinalPowerDownFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerFinal"></a><a id="wdfdevstatepowerfinal"></a><a id="WDFDEVSTATEPOWERFINAL"></a><b>WdfDevStatePowerFinal</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoImplicitD3DisarmWakeAtBus"></a><a id="wdfdevstatepowergotoimplicitd3disarmwakeatbus"></a><a id="WDFDEVSTATEPOWERGOTOIMPLICITD3DISARMWAKEATBUS"></a><b>WdfDevStatePowerGotoImplicitD3DisarmWakeAtBus</b>

<dd></dd>

### -field <a id="WdfDevStatePowerUpFailed"></a><a id="wdfdevstatepowerupfailed"></a><a id="WDFDEVSTATEPOWERUPFAILED"></a><b>WdfDevStatePowerUpFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerUpFailedDerefParent"></a><a id="wdfdevstatepowerupfailedderefparent"></a><a id="WDFDEVSTATEPOWERUPFAILEDDEREFPARENT"></a><b>WdfDevStatePowerUpFailedDerefParent</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxFailed"></a><a id="wdfdevstatepowergotodxfailed"></a><a id="WDFDEVSTATEPOWERGOTODXFAILED"></a><b>WdfDevStatePowerGotoDxFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePowerGotoDxStoppedDisableInterrupt"></a><a id="wdfdevstatepowergotodxstoppeddisableinterrupt"></a><a id="WDFDEVSTATEPOWERGOTODXSTOPPEDDISABLEINTERRUPT"></a><b>WdfDevStatePowerGotoDxStoppedDisableInterrupt</b>

<dd></dd>

### -field <a id="WdfDevStatePowerUpFailedNP"></a><a id="wdfdevstatepowerupfailednp"></a><a id="WDFDEVSTATEPOWERUPFAILEDNP"></a><b>WdfDevStatePowerUpFailedNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerUpFailedDerefParentNP"></a><a id="wdfdevstatepowerupfailedderefparentnp"></a><a id="WDFDEVSTATEPOWERUPFAILEDDEREFPARENTNP"></a><b>WdfDevStatePowerUpFailedDerefParentNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerNotifyingD0ExitToWakeInterrupts"></a><a id="wdfdevstatepowernotifyingd0exittowakeinterrupts"></a><a id="WDFDEVSTATEPOWERNOTIFYINGD0EXITTOWAKEINTERRUPTS"></a><b>WdfDevStatePowerNotifyingD0ExitToWakeInterrupts</b>

<dd></dd>

### -field <a id="WdfDevStatePowerNotifyingD0EntryToWakeInterrupts"></a><a id="wdfdevstatepowernotifyingd0entrytowakeinterrupts"></a><a id="WDFDEVSTATEPOWERNOTIFYINGD0ENTRYTOWAKEINTERRUPTS"></a><b>WdfDevStatePowerNotifyingD0EntryToWakeInterrupts</b>

<dd></dd>

### -field <a id="WdfDevStatePowerNotifyingD0ExitToWakeInterruptsNP"></a><a id="wdfdevstatepowernotifyingd0exittowakeinterruptsnp"></a><a id="WDFDEVSTATEPOWERNOTIFYINGD0EXITTOWAKEINTERRUPTSNP"></a><b>WdfDevStatePowerNotifyingD0ExitToWakeInterruptsNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerNotifyingD0EntryToWakeInterruptsNP"></a><a id="wdfdevstatepowernotifyingd0entrytowakeinterruptsnp"></a><a id="WDFDEVSTATEPOWERNOTIFYINGD0ENTRYTOWAKEINTERRUPTSNP"></a><b>WdfDevStatePowerNotifyingD0EntryToWakeInterruptsNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerInitialPowerUpFailedPowerDown"></a><a id="wdfdevstatepowerinitialpowerupfailedpowerdown"></a><a id="WDFDEVSTATEPOWERINITIALPOWERUPFAILEDPOWERDOWN"></a><b>WdfDevStatePowerInitialPowerUpFailedPowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePowerUpFailedPowerDown"></a><a id="wdfdevstatepowerupfailedpowerdown"></a><a id="WDFDEVSTATEPOWERUPFAILEDPOWERDOWN"></a><b>WdfDevStatePowerUpFailedPowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePowerUpFailedPowerDownNP"></a><a id="wdfdevstatepowerupfailedpowerdownnp"></a><a id="WDFDEVSTATEPOWERUPFAILEDPOWERDOWNNP"></a><b>WdfDevStatePowerUpFailedPowerDownNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerInitialSelfManagedIoFailedStarted"></a><a id="wdfdevstatepowerinitialselfmanagediofailedstarted"></a><a id="WDFDEVSTATEPOWERINITIALSELFMANAGEDIOFAILEDSTARTED"></a><b>WdfDevStatePowerInitialSelfManagedIoFailedStarted</b>

<dd></dd>

### -field <a id="WdfDevStatePowerStartSelfManagedIoFailedStarted"></a><a id="wdfdevstatepowerstartselfmanagediofailedstarted"></a><a id="WDFDEVSTATEPOWERSTARTSELFMANAGEDIOFAILEDSTARTED"></a><b>WdfDevStatePowerStartSelfManagedIoFailedStarted</b>

<dd></dd>

### -field <a id="WdfDevStatePowerStartSelfManagedIoFailedStartedNP"></a><a id="wdfdevstatepowerstartselfmanagediofailedstartednp"></a><a id="WDFDEVSTATEPOWERSTARTSELFMANAGEDIOFAILEDSTARTEDNP"></a><b>WdfDevStatePowerStartSelfManagedIoFailedStartedNP</b>

<dd></dd>

### -field <a id="WdfDevStatePowerNull"></a><a id="wdfdevstatepowernull"></a><a id="WDFDEVSTATEPOWERNULL"></a><b>WdfDevStatePowerNull</b>

<dd></dd>
</dl>

## -remarks
<p>The <b>WDF_DEVICE_POWER_STATE</b> enumeration is used as a member type in the <a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-notification-data.md">WDF_DEVICE_POWER_NOTIFICATION_DATA</a> structure and as the return type for the <a href="..\wdfdevice\nf-wdfdevice-wdfdevicegetdevicepowerstate.md">WdfDeviceGetDevicePowerState</a> method.</p>

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