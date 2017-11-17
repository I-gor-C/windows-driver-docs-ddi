# Declarations in the portcls header
This header Portcls contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [IMiniportWaveCyclicStream::SetState method](nf-portcls-iminiportwavecyclicstream-setstate.md) | The SetState method sets the new state of playback or recording for the stream. |
| [PcNewMiniport function](nf-portcls-pcnewminiport.md) | The PcNewMiniport function creates an instance of one of the system-supplied miniport drivers that are built into the PortCls system driver, portcls.sys. |
| [FindTranslatedDevicePrivate function](nf-portcls-findtranslateddeviceprivate.md) | TBD |
| [IInterruptSync::Connect method](nf-portcls-iinterruptsync-connect.md) | The Connect method connects the synchronization object to the interrupt. |
| [AddPortFromParent function](nf-portcls-addportfromparent.md) | TBD |
| [IResourceList::NumberOfEntriesOfType method](nf-portcls-iresourcelist-numberofentriesoftype.md) | The NumberOfEntriesOfType method returns the number of resource items of a given type in the resource list. For each resource type, a macro is defined to call this method as previously described. |
| [InitializeAdapterDriver function](nf-portcls-initializeadapterdriver.md) | TBD |
| [IMiniportWaveRTStreamNotification::UnregisterNotificationEvent method](nf-portcls-iminiportwavertstreamnotification-unregisternotificationevent.md) | The UnregisterNotificationEvent method unregisters an event from DMA driven event notification. |
| [IPortWavePci::Notify method](nf-portcls-iportwavepci-notify~r2.md) | TBD |
| [IServiceSink::RequestService method](nf-portcls-iservicesink-requestservice.md) | The RequestService method is called to forward a service request to an IServiceSink object. |
| [IMiniportAudioEngineNode::GetDeviceChannelMute method](nf-portcls-iminiportaudioenginenode-getdevicechannelmute.md) | Gets the state of the Mute node for the audio device channel. |
| [IPortEvents::AddEventToEventList method](nf-portcls-iportevents-addeventtoeventlist.md) | The AddEventToEventList method adds an event to the port driver's event list. |
| [WIN95COMPAT_WritePortUShort function](nf-portcls-win95compat-writeportushort.md) | TBD |
| [FindUntranslatedInterrupt function](nf-portcls-finduntranslatedinterrupt.md) | TBD |
| [IMiniportStreamAudioEngineNode::SetLfxState method](nf-portcls-iminiportstreamaudioenginenode-setlfxstate.md) | Sets the state of the local effects (LFX) node that is in the path of the audio stream. |
| [IMiniportAudioEngineNode::GetDeviceChannelVolume method](nf-portcls-iminiportaudioenginenode-getdevicechannelvolume.md) | Gets the volume level for a given channel of the audio device. |
| [IPortWavePci::NewMasterDmaChannel method](nf-portcls-iportwavepci-newmasterdmachannel~r1.md) | TBD |
| [IPortWaveCyclic::Notify method](nf-portcls-iportwavecyclic-notify.md) | The Notify method notifies the port driver that an interrupt indicating the progress of the DMA pointer has occurred. It should be called from the miniport driver's interrupt service routine (ISR). |
| [IMiniportWaveRTStreamNotification::RegisterNotificationEvent method](nf-portcls-iminiportwavertstreamnotification-registernotificationevent.md) | The RegisterNotificationEvent method registers an event to be notified for DMA-driven event notification. |
| [IMiniportWaveCyclic::Init method](nf-portcls-iminiportwavecyclic-init.md) | The Init method initializes the WaveCyclic miniport object. Initialization includes verification of the hardware using the resources specified in the resource list. |
| [PcUnregisterAdapterPnpManagement function](nf-portcls-pcunregisteradapterpnpmanagement.md) | The PcUnregisterAdapterPnpManagement function unregisters the audio adapter's PnP management interface from the PortCls class driver. It is used to support PnP rebalance. |
| [IMiniportWavePci::NewStream method](nf-portcls-iminiportwavepci-newstream.md) | The NewStream method creates a new instance of a logical stream associated with a specified physical channel. |
| [FindTranslatedAssignedResource function](nf-portcls-findtranslatedassignedresource.md) | TBD |
| [IPortWavePci::Notify method](nf-portcls-iportwavepci-notify.md) | The Notify method notifies the port driver that an interrupt indicating the progress of the DMA pointer has occurred. |
| [PcNewPort function](nf-portcls-pcnewport.md) | The PcNewPort function creates a new system-supplied port-driver object, whose interface (derived from base class IPort) is specified by a class ID. |
| [IPortClsRuntimePower::UnregisterPowerControlCallback method](nf-portcls-iportclsruntimepower-unregisterpowercontrolcallback.md) | The port class driver (PortCls) uses the UnregisterPowerControlCallback method to unregister a power control callback. |
| [IServiceGroup::RemoveMember method](nf-portcls-iservicegroup-removemember.md) | The RemoveMember method removes the specified member from the service group. |
| [PcDestroyContent function](nf-portcls-pcdestroycontent.md) | The PcDestroyContent function deletes a DRM content ID that was created by PcCreateContentMixed. Note that this function call is identical in operation to the DrmDestroyContent function, and its parameter definitions and return value are also identical. |
| [IMiniportWaveRT::Init method](nf-portcls-iminiportwavert-init~r4.md) | TBD |
| [IMiniportWaveCyclic::Init method](nf-portcls-iminiportwavecyclic-init~r2.md) | TBD |
| [PcRegisterAdapterPnpManagement function](nf-portcls-pcregisteradapterpnpmanagement.md) | The PcRegisterAdapterPnpManagement function registers the adapter's PnP-management interface with the PortCls system driver. It is used to support PnP rebalance. |
| [FindTranslatedMemory function](nf-portcls-findtranslatedmemory.md) | TBD |
| [PcRequestNewPowerState function](nf-portcls-pcrequestnewpowerstate.md) | The PcRequestNewPowerState function is used to request a new power state for the device. This function is typically not needed by adapter drivers but can occasionally be useful in working around some kinds of hardware problems. |
| [PcUnregisterIoTimeout function](nf-portcls-pcunregisteriotimeout.md) | The PcUnregisterIoTimeout function unregisters a driver-supplied I/O-timer callback routine for a specified device object. |
| [PcNewResourceList function](nf-portcls-pcnewresourcelist.md) | The PcNewResourceList function creates and initializes a resource list. |
| [IResourceList::AddEntryFromParent method](nf-portcls-iresourcelist-addentryfromparent.md) | The AddEntryFromParent method adds to a resource list an entry found in the resource list's parent list. |
| [IResourceList::TranslatedList method](nf-portcls-iresourcelist-translatedlist.md) | The TranslatedList method returns the list of translated resources. |
| [PcCompletePendingPropertyRequest function](nf-portcls-pccompletependingpropertyrequest.md) | The PcCompletePendingPropertyRequest function is called to complete a pending property request. |
| [IPortWavePciStream::TerminatePacket method](nf-portcls-iportwavepcistream-terminatepacket.md) | The TerminatePacket method terminates the packet currently being mapped. |
| [IPortClsPnp::RegisterAdapterPnpManagement method](nf-portcls-iportclspnp-registeradapterpnpmanagement.md) | The RegisterAdapterPowerManagement method registers the PnP management interface of the adapter with PortCls. |
| [IPortClsRuntimePower::RegisterPowerControlCallback method](nf-portcls-iportclsruntimepower-registerpowercontrolcallback.md) | The port class driver (PortCls) uses the RegisterPowerControlCallback method to register a power control callback. |
| [PcGetTimeInterval function](nf-portcls-pcgettimeinterval.md) | The PcGetTimeInterval function returns the time elapsed since a specified time. Time is measured in 100-nanosecond units. |
| [IMiniportAudioEngineNode::GetDeviceAttributeSteppings method](nf-portcls-iminiportaudioenginenode-getdeviceattributesteppings.md) | Gets the allowed stepping value for the audio device attribute. |
| [IServiceGroup::RequestService method](nf-portcls-iservicegroup-requestservice.md) | TBD |
| [IMiniportWavePci::Init method](nf-portcls-iminiportwavepci-init.md) | The Init method initializes the WavePci miniport object. Initialization includes verification of the hardware using the resources specified in the resource list. |
| [IMiniportWavePciStream::SetState method](nf-portcls-iminiportwavepcistream-setstate~r2.md) | TBD |
| [PcNewServiceGroup function](nf-portcls-pcnewservicegroup.md) | The PcNewServiceGroup function creates and initializes a service group. |
| [IMiniportWaveRT::Init method](nf-portcls-iminiportwavert-init.md) | The Init method initializes the WaveRT miniport driver object. |
| [FindUntranslatedDevicePrivate function](nf-portcls-finduntranslateddeviceprivate.md) | TBD |
| [IMiniportWaveRT::GetDeviceDescription method](nf-portcls-iminiportwavert-getdevicedescription.md) | The GetDeviceDescription method returns a pointer to a DEVICE_DESCRIPTION structure describing the device. |
| [IPortClsRuntimePower::SendPowerControl method](nf-portcls-iportclsruntimepower-sendpowercontrol.md) | The port class driver (PortCls) uses the SendPowerControl method to send power control codes to the audio adapter. |
| [IMiniportStreamAudioEngineNode::GetStreamLinearBufferPosition method](nf-portcls-iminiportstreamaudioenginenode-getstreamlinearbufferposition.md) | Gets the number of bytes that the DMA has fetched from the audio buffer since the beginning of the stream. |
| [IResourceList::FindTranslatedEntry method](nf-portcls-iresourcelist-findtranslatedentry.md) | The FindTranslatedEntry method returns a pointer to a translated entry of the specified type, or NULL if no such entry is found. |
| [IMiniportWaveCyclicStream::SetState method](nf-portcls-iminiportwavecyclicstream-setstate~r1.md) | TBD |
| [IMiniportWaveCyclic::NewStream method](nf-portcls-iminiportwavecyclic-newstream~r1.md) | TBD |
| [RegisterPhysicalConnection function](nf-portcls-registerphysicalconnection.md) | TBD |
| [IMiniportAudioSignalProcessing::GetModes method](nf-portcls-iminiportaudiosignalprocessing-getmodes.md) | The GetModes method, Gets the audio signal processing modes supported by an audio pin. |
| [IInterruptSync::RegisterServiceRoutine method](nf-portcls-iinterruptsync-registerserviceroutine.md) | The RegisterServiceRoutine method registers an interrupt service routine (ISR) that is to be called when an interrupt occurs. |
| [PcInitializeAdapterDriver function](nf-portcls-pcinitializeadapterdriver.md) | The PcInitializeAdapterDriver function binds an adapter driver to the PortCls system driver. |
| [PcRegisterPhysicalConnectionFromExternal function](nf-portcls-pcregisterphysicalconnectionfromexternal.md) | The PcRegisterPhysicalConnectionFromExternal function registers a physical connection to an audio adapter filter from an external audio adapter filter. |
| [IUnregisterSubdevice::UnregisterSubdevice method](nf-portcls-iunregistersubdevice-unregistersubdevice.md) | The UnregisterSubdevice method deletes the registration of a subdevice that was previously registered by a call to PcRegisterSubdevice. |
| [GTI_SECONDS function](nf-portcls-gti-seconds.md) | TBD |
| [IMiniportAudioEngineNode::GetGfxState method](nf-portcls-iminiportaudioenginenode-getgfxstate.md) | Gets the state of the global effects (GFX) node in the audio engine. |
| [IPortClsSubdeviceEx::UpdatePinDescriptor method](nf-portcls-iportclssubdeviceex-updatepindescriptor.md) | TBD |
| [IMiniportAudioEngineNode::GetDeviceChannelCount method](nf-portcls-iminiportaudioenginenode-getdevicechannelcount.md) | Gets a count of the number of channels supported by the audio device. |
| [IAdapterPowerManagement::QueryPowerChangeState method](nf-portcls-iadapterpowermanagement-querypowerchangestate.md) | The QueryPowerChangeState method is called by PortCls in response to the receipt of an IRP_MN_QUERY_POWER power IRP. |
| [IMiniportAudioEngineNode::GetAudioEngineDescriptor method](nf-portcls-iminiportaudioenginenode-getaudioenginedescriptor.md) | Gets the descriptor for the audio engine node. |
| [IMiniportWavePci::NewStream method](nf-portcls-iminiportwavepci-newstream~r2.md) | TBD |
| [IDrmPort2::AddContentHandlers method](nf-portcls-idrmport2-addcontenthandlers.md) | The AddContentHandlers method provides the system with a list of functions that handle protected content. |
| [IRegistryKey::EnumerateKey method](nf-portcls-iregistrykey-enumeratekey.md) | The EnumerateKey method returns information about the subkeys of the open key. |
| [PcNewRegistryKey function](nf-portcls-pcnewregistrykey.md) | The PcNewRegistryKey function opens or creates a new registry key and creates an IRegistryKey object to represent the key. The caller accesses the key through this object. |
| [PcAddAdapterDevice function](nf-portcls-pcaddadapterdevice.md) | The PcAddAdapterDevice function adds an adapter device to the WDM device stack. |
| [FindTranslatedDeviceSpecific function](nf-portcls-findtranslateddevicespecific.md) | TBD |
| [IPortWaveRTStream::FreePagesFromMdl method](nf-portcls-iportwavertstream-freepagesfrommdl.md) | The FreePagesFromMdl method frees a memory descriptor list (MDL). |
| [PcRegisterPhysicalConnectionToExternal function](nf-portcls-pcregisterphysicalconnectiontoexternal.md) | The PcRegisterPhysicalConnectionToExternal function registers a physical connection from an audio adapter filter to an external audio adapter filter. |
| [IMiniportStreamAudioEngineNode::SetStreamChannelMute method](nf-portcls-iminiportstreamaudioenginenode-setstreamchannelmute.md) | Sets the state of the Mute node in the path of the audio stream. |
| [IPortWMIRegistration::RegisterWMIProvider method](nf-portcls-iportwmiregistration-registerwmiprovider.md) | The RegisterWMIProvider method registers the Event Tracing for Windows (ETW) capability of the miniport driver with PortCls. |
| [PcCreateContentMixed function](nf-portcls-pccreatecontentmixed.md) | The PcCreateContentMixed function computes the DRM content rights for a composite stream containing mixed content from some number of KS audio streams. |
| [IPortWaveCyclic::Notify method](nf-portcls-iportwavecyclic-notify~r1.md) | TBD |
| [IMiniportAudioEngineNode::GetDeviceFormat method](nf-portcls-iminiportaudioenginenode-getdeviceformat.md) | Gets the audio data format for an audio device. |
| [PC_POWER_FRAMEWORK_SETTINGS_INIT function](nf-portcls-pc-power-framework-settings-init.md) | TBD |
| [IMiniportWavePci::Service method](nf-portcls-iminiportwavepci-service.md) | The Service method notifies the miniport driver of a request for service. |
| [IMiniportWavePciStream::SetFormat method](nf-portcls-iminiportwavepcistream-setformat.md) | The SetFormat method sets the KS data format of the wave stream. |
| [PcDispatchIrp function](nf-portcls-pcdispatchirp.md) | The PcDispatchIrp function dispatches an IRP to the PortCls system driver's default handler. |
| [PcForwardContentToInterface function](nf-portcls-pcforwardcontenttointerface.md) | The PcForwardContentToInterface function accepts a pointer to the COM interface of an object to which the caller intends to forward protected content. |
| [PcForwardContentToDeviceObject function](nf-portcls-pcforwardcontenttodeviceobject.md) | The PcForwardContentToDeviceObject function accepts a device object representing a device to which the caller intends to forward protected content. |
| [IPortClsPnp::UnregisterAdapterPnpManagement method](nf-portcls-iportclspnp-unregisteradapterpnpmanagement.md) | The UnRegisterAdapterPowerManagement method unregisters the PnP management interface of the adapter from PortCls. |
| [IPortClsPower::SetIdlePowerManagement method](nf-portcls-iportclspower-setidlepowermanagement.md) | The SetIdlePowerManagement method provides a way for the adapter driver to opt in or opt out of idle state detection. |
| [IMiniportStreamAudioEngineNode::GetStreamChannelMute method](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelmute.md) | Gets the state of the Mute node in the path of the audio stream. |
| [PcNewResourceSublist function](nf-portcls-pcnewresourcesublist.md) | The PcNewResourceSublist function creates and initializes an empty resource list that is derived from another resource list. |
| [PcGetDeviceProperty function](nf-portcls-pcgetdeviceproperty.md) | The PcGetDeviceProperty function returns the requested device property from the registry. |
| [IMiniportWavePciStream::MappingAvailable method](nf-portcls-iminiportwavepcistream-mappingavailable.md) | The MappingAvailable method indicates that a new mapping is available. |
| [FindTranslatedBusNumber function](nf-portcls-findtranslatedbusnumber.md) | TBD |
| [IMiniportWaveRTOutputStream::GetOutputStreamPresentationPosition method](nf-portcls-iminiportwavertoutputstream-getoutputstreampresentationposition.md) | Returns stream presentation information. |
| [DEFINE_PCAUTOMATION_TABLE_EVENT function](nf-portcls-define-pcautomation-table-event.md) | TBD |
| [RegisterSubdevice function](nf-portcls-registersubdevice.md) | TBD |
| [IMiniportStreamAudioEngineNode::SetStreamChannelVolume method](nf-portcls-iminiportstreamaudioenginenode-setstreamchannelvolume.md) | Sets the volume level to be applied to the audio stream. |
| [IInterruptSync::Disconnect method](nf-portcls-iinterruptsync-disconnect.md) | The Disconnect method disconnects the synchronization object from the interrupt. |
| [IMiniportStreamAudioEngineNode2::SetStreamCurrentWritePositionForLastBuffer method](nf-portcls-iminiportstreamaudioenginenode2-setstreamcurrentwritepositionforlastbuffer.md) | Sets the current cursor position in the last audio data stream that was written to the audio buffer. |
| [IPinCount::PinCount method](nf-portcls-ipincount-pincount.md) | The PinCount method queries the miniport driver for its pin count. |
| [IPortClsPower::UnregisterAdapterPowerManagement method](nf-portcls-iportclspower-unregisteradapterpowermanagement.md) | The UnregisterAdapterPowerManagement method unregisters the adapter's power management interface with PortCls. |
| [DEFINE_PCAUTOMATION_TABLE_PROP_EVENT function](nf-portcls-define-pcautomation-table-prop-event.md) | TBD |
| [IPortWaveCyclic::NewMasterDmaChannel method](nf-portcls-iportwavecyclic-newmasterdmachannel.md) | The NewMasterDmaChannel method creates a new instance of a bus-master DMA channel. |
| [IMiniportAudioEngineNode::GetSupportedDeviceFormats method](nf-portcls-iminiportaudioenginenode-getsupporteddeviceformats.md) | Gets the supported audio data formats for the audio device. |
| [IAdapterPowerManagement2::PowerChangeState2 method](nf-portcls-iadapterpowermanagement2-powerchangestate2.md) | Portcls calls the IAdapterPowerManagement2 |
| [IPortWavePciStream::ReleaseMapping method](nf-portcls-iportwavepcistream-releasemapping.md) | The ReleaseMapping method releases a mapping that was obtained by a previous call to IPortWavePciStream |
| [IMiniportMidiStream::SetFormat method](nf-portcls-iminiportmidistream-setformat.md) | The SetFormat method sets the KS data format of the MIDI stream. |
| [FindTranslatedSubAllocateFrom function](nf-portcls-findtranslatedsuballocatefrom.md) | TBD |
| [IPortMidi::Notify method](nf-portcls-iportmidi-notify.md) | The Notify method notifies the port driver that an interrupt indicating the progress of the DMA pointer has occurred. It should be called from the miniport driver's interrupt service routine (ISR). |
| [IDrmPort2::ForwardContentToDeviceObject method](nf-portcls-idrmport2-forwardcontenttodeviceobject.md) | The ForwardContentToDeviceObject method accepts a device object representing a device to which the caller intends to forward protected content. |
| [IMiniportWaveRTOutputStream::GetPacketCount method](nf-portcls-iminiportwavertoutputstream-getpacketcount.md) | GetPacketCount returns the (1-based) count of packets completely transferred from the WaveRT buffer into hardware. |
| [IMiniportStreamAudioEngineNode::GetStreamAttributeSteppings method](nf-portcls-iminiportstreamaudioenginenode-getstreamattributesteppings.md) | Gets the allowed stepping value for the audio stream attribute. |
| [IPortWMIRegistration::UnregisterWMIProvider method](nf-portcls-iportwmiregistration-unregisterwmiprovider.md) | The UnregisterWMIProvider method unregisters the Event Tracing for Windows (ETW) interface that was previously registered with a call to the RegisterWMIProvider method. The unregistration disables the ETW registration with PortCls. |
| [FindUntranslatedAssignedResource function](nf-portcls-finduntranslatedassignedresource.md) | TBD |
| [PcUnregisterAdapterPowerManagement function](nf-portcls-pcunregisteradapterpowermanagement.md) | The PcUnregisterAdapterPowerManagement function unregisters the audio adapter's power management interface from the PortCls class driver. The PcUnregisterAdapterPowerManagement function is available in Windows 7 and later versions of Windows. |
| [IPortEvents::GenerateEventList method](nf-portcls-iportevents-generateeventlist.md) | The GenerateEventList method notifies clients through the port driver's list of event entries that a particular event has occurred. |
| [AddAdapterDevice function](nf-portcls-addadapterdevice.md) | TBD |
| [FindTranslatedInterrupt function](nf-portcls-findtranslatedinterrupt.md) | TBD |
| [IMiniportWavePciStream::NormalizePhysicalPosition method](nf-portcls-iminiportwavepcistream-normalizephysicalposition~r1.md) | TBD |
| [IMiniportWavePciStream::SetFormat method](nf-portcls-iminiportwavepcistream-setformat~r2.md) | TBD |
| [IRegistryKey::DeleteKey method](nf-portcls-iregistrykey-deletekey.md) | The DeleteKey method deletes the registry key. |
| [IPortWavePci::NewMasterDmaChannel method](nf-portcls-iportwavepci-newmasterdmachannel.md) | The NewMasterDmaChannel method creates a new instance of a bus-master DMA channel. |
| [RegisterPhysicalConnectionToExternal function](nf-portcls-registerphysicalconnectiontoexternal.md) | TBD |
| [IPortWaveRTStream::AllocateContiguousPagesForMdl method](nf-portcls-iportwavertstream-allocatecontiguouspagesformdl.md) | The AllocateContiguousPagesForMdl method allocates a list of contiguous, nonpaged, physical memory pages and returns a pointer to a memory descriptor list (MDL) that describes them. |
| [IPowerNotify::PowerChangeNotify method](nf-portcls-ipowernotify-powerchangenotify.md) | The PowerChangeNotify method notifies the miniport driver of changes in the power state. |
| [AddSubAllocateFromFromParent function](nf-portcls-addsuballocatefromfromparent.md) | TBD |
| [IMiniportStreamAudioEngineNode::GetStreamChannelPeakMeter method](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelpeakmeter.md) | Gets the value of the PeakMeter node in the path of the audio stream. |
| [IMiniportStreamAudioEngineNode::GetLfxState method](nf-portcls-iminiportstreamaudioenginenode-getlfxstate.md) | Gets the state of the local effects (LFX) node that is in the path of the audio stream. |
| [IResourceList::AddEntry method](nf-portcls-iresourcelist-addentry.md) | The AddEntry method adds an entry to a resource list. |
| [IMiniportWavePciStream::RevokeMappings method](nf-portcls-iminiportwavepcistream-revokemappings.md) | The RevokeMappings method revokes mappings that were previously obtained through IPortWavePciStream |
| [IAdapterPowerManagement3::D3ExitLatencyChanged method](nf-portcls-iadapterpowermanagement3-d3exitlatencychanged.md) | PortCls calls the D3ExitLatencyChanged method while the device is in sleep (D3) power state, to provide a new exit latency value. |
| [IMiniportMidi::Service method](nf-portcls-iminiportmidi-service.md) | The Service method notifies the miniport driver of a request for service. |
| [IAdapterPowerManagement::PowerChangeState method](nf-portcls-iadapterpowermanagement-powerchangestate.md) | The PowerChangeState method requests that the device change to a new power state. |
| [WIN95COMPAT_ReadPortUChar function](nf-portcls-win95compat-readportuchar.md) | TBD |
| [IRegistryKey::QueryRegistryValues method](nf-portcls-iregistrykey-queryregistryvalues.md) | The QueryRegistryValues method allows the caller to query several values from the registry with a single call. |
| [IPortClsVersion::GetVersion method](nf-portcls-iportclsversion-getversion.md) | The GetVersion method returns the version of the Windows operating system that the driver is running on. |
| [IMiniportTopology::Init method](nf-portcls-iminiporttopology-init~r1.md) | TBD |
| [IPortWaveCyclic::NewSlaveDmaChannel method](nf-portcls-iportwavecyclic-newslavedmachannel.md) | The NewSlaveDmaChannel method creates a new instance of a subordinate DMA channel. |
| [IMiniportWavePciStream::NormalizePhysicalPosition method](nf-portcls-iminiportwavepcistream-normalizephysicalposition.md) | The NormalizePhysicalPosition method converts a physical buffer position to a time-based value. |
| [IInterruptSync::CallSynchronizedRoutine method](nf-portcls-iinterruptsync-callsynchronizedroutine.md) | The CallSynchronizedRoutine method calls a routine that is not an interrupt service routine (ISR) but whose execution needs to be synchronized with ISRs. |
| [IServiceGroup::RequestDelayedService method](nf-portcls-iservicegroup-requestdelayedservice.md) | The RequestDelayedService method requests service after the specified delay. |
| [AddDeviceSpecificFromParent function](nf-portcls-adddevicespecificfromparent.md) | TBD |
| [IResourceList::FindUntranslatedEntry method](nf-portcls-iresourcelist-finduntranslatedentry.md) | The FindUntranslatedEntry method returns a pointer to an untranslated entry of the specified type, or NULL if no such pointer is found. |
| [IMiniportAudioEngineNode::GetEngineFormatSize method](nf-portcls-iminiportaudioenginenode-getengineformatsize.md) | Gets the format type and the buffer size for the audio engine's audio data format. |
| [IMiniportMidiStream::SetState method](nf-portcls-iminiportmidistream-setstate.md) | The SetState method sets the stream's transport state to a new state value. |
| [AddDevicePrivateFromParent function](nf-portcls-adddeviceprivatefromparent.md) | TBD |
| [AddDmaFromParent function](nf-portcls-adddmafromparent.md) | TBD |
| [IPortClsNotifications::SendNotification method](nf-portcls-iportclsnotifications-sendnotification.md) | Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps. |
| [FindUntranslatedMemory function](nf-portcls-finduntranslatedmemory.md) | TBD |
| [IUnregisterPhysicalConnection::UnregisterPhysicalConnection method](nf-portcls-iunregisterphysicalconnection-unregisterphysicalconnection.md) | The UnregisterPhysicalConnection method deletes the registration of a physical connection that was registered by a previous call to PcRegisterPhysicalConnection. |
| [IMiniportStreamAudioEngineNode::GetStreamPresentationPosition method](nf-portcls-iminiportstreamaudioenginenode-getstreampresentationposition.md) | Gets the current cursor position in the audio data stream that is being rendered to the endpoint. |
| [IPortClsNotifications::FreeNotificationBuffer method](nf-portcls-iportclsnotifications-freenotificationbuffer.md) | Frees a previously allocated IPortClsNotifications buffer. The buffer is used in sending notifications, to allow for communications between audio modules and UWP apps. |
| [GTI_MILLISECONDS function](nf-portcls-gti-milliseconds.md) | TBD |
| [PcForwardIrpSynchronous function](nf-portcls-pcforwardirpsynchronous.md) | The PcForwardIrpSynchronous function is used by IRP handlers to forward Plug and Play IRPs to the physical device object (PDO). |
| [IUnregisterPhysicalConnection::UnregisterPhysicalConnectionToExternal method](nf-portcls-iunregisterphysicalconnection-unregisterphysicalconnectiontoexternal.md) | The UnregisterPhysicalConnectionToExternal method deletes the registration of a physical connection that was registered by a previous call to PcRegisterPhysicalConnectionToExternal. |
| [IPortClsStreamResourceManager2::AddStreamResource2 method](nf-portcls-iportclsstreamresourcemanager2-addstreamresource2.md) | AddStreamResource2 adds a stream resource. Two type of stream resources are supported |
| [FindTranslatedPort function](nf-portcls-findtranslatedport.md) | TBD |
| [IPortWavePciStream::GetMapping method](nf-portcls-iportwavepcistream-getmapping.md) | The GetMapping method obtains a mapping from the port driver and associates a tag with the mapping. |
| [IMiniportMidiStream::Read method](nf-portcls-iminiportmidistream-read.md) | The Read method reads data from an incoming MIDI stream. |
| [IMiniportWaveRTStreamNotification::FreeBufferWithNotification method](nf-portcls-iminiportwavertstreamnotification-freebufferwithnotification.md) | The FreeBufferWithNotification method is used to free an audio buffer previously allocated with a call to IMiniportWaveRTStreamNotification |
| [PcNewDmaChannel function](nf-portcls-pcnewdmachannel.md) | The PcNewDmaChannel function creates a new DMA-channel object. This function is obsolete; for more information, see the following comments. |
| [IMiniportWaveRTStreamNotification::AllocateBufferWithNotification method](nf-portcls-iminiportwavertstreamnotification-allocatebufferwithnotification.md) | The AllocateAudioBufferWithNotification method allocates a cyclic buffer for audio data when you want to implement DMA-driven event notification. If you do not want event notification, you must use IMiniportWaveRTStream |
| [IPortClsEtwHelper::MiniportWriteEtwEvent method](nf-portcls-iportclsetwhelper-miniportwriteetwevent.md) | The MiniportWriteEtwEvent method is used by an audio miniport driver for providing the information about an Event Tracing for Windows (ETW) event. |
| [IAdapterPowerManagement::QueryDeviceCapabilities method](nf-portcls-iadapterpowermanagement-querydevicecapabilities.md) | The QueryDeviceCapabilities method is called by PortCls in response to a Plug and Play IRP_MN_QUERY_CAPABILITIES IRP. |
| [IMiniportWaveRTInputStream::GetReadPacket method](nf-portcls-iminiportwavertinputstream-getreadpacket.md) | Returns information about captured data. |
| [FindUntranslatedDma function](nf-portcls-finduntranslateddma.md) | TBD |
| [FindUntranslatedPort function](nf-portcls-finduntranslatedport.md) | TBD |
| [IMiniportMidiStream::Write method](nf-portcls-iminiportmidistream-write.md) | The Write method writes data to an outgoing MIDI stream. |
| [IMusicTechnology::SetTechnology method](nf-portcls-imusictechnology-settechnology.md) | The SetTechnology method changes the Technology member of each KSDATARANGE_MUSIC structure in the data ranges for the miniport driver's pins. |
| [RegisterPhysicalConnectionFromExternal function](nf-portcls-registerphysicalconnectionfromexternal.md) | TBD |
| [IServiceGroup::SupportDelayedService method](nf-portcls-iservicegroup-supportdelayedservice.md) | The SupportDelayedService method indicates that the service group should prepare to support delayed service. |
| [IMiniportAudioEngineNode::GetBufferSizeRange method](nf-portcls-iminiportaudioenginenode-getbuffersizerange.md) | Gets the minimum and maximum buffer size that the hardware audio engine can support. |
| [IPortWaveRTStream::GetPhysicalPagesCount method](nf-portcls-iportwavertstream-getphysicalpagescount.md) | The GetPhysicalPagesCount method returns the count of the physical pages in a memory descriptor list (MDL). |
| [IMiniportStreamAudioEngineNode::SetStreamLoopbackProtection method](nf-portcls-iminiportstreamaudioenginenode-setstreamloopbackprotection.md) | Sets the loopback protection status of the audio engine node. |
| [FindUntranslatedBusNumber function](nf-portcls-finduntranslatedbusnumber.md) | TBD |
| [AddInterruptFromParent function](nf-portcls-addinterruptfromparent.md) | TBD |
| [IMiniportWaveCyclicStream::SetFormat method](nf-portcls-iminiportwavecyclicstream-setformat.md) | The SetFormat method sets the KS data format of the wave stream. |
| [IPortMidi::RegisterServiceGroup method](nf-portcls-iportmidi-registerservicegroup.md) | The RegisterServiceGroup method registers the service group to be used for the IPortMidi |
| [IPortWaveRTStream::MapAllocatedPages method](nf-portcls-iportwavertstream-mapallocatedpages.md) | The MapAllocatedPages method maps a list of previously allocated physical pages into a contiguous block of virtual memory that is accessible from kernel-mode. |
| [PcCompleteIrp function](nf-portcls-pccompleteirp.md) | The PcCompleteIrp function completes an IRP that was previously marked as pending. |
| [IMiniportAudioEngineNode::GetMixFormat method](nf-portcls-iminiportaudioenginenode-getmixformat.md) | Gets the audio data format for the audio engine mixer. |
| [PcRegisterPhysicalConnection function](nf-portcls-pcregisterphysicalconnection.md) | The PcRegisterPhysicalConnection function registers a physical connection between two audio adapter filters that are instantiated by the same adapter driver. |
| [IMiniportWavePci::Init method](nf-portcls-iminiportwavepci-init~r3.md) | TBD |
| [IMiniportStreamAudioEngineNode::GetStreamChannelCount method](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelcount.md) | Gets a count of the number of channels available for the stream. |
| [IMiniportAudioEngineNode::SetDeviceChannelVolume method](nf-portcls-iminiportaudioenginenode-setdevicechannelvolume.md) | Sets the volume level for a given channel of the audio device. |
| [IRegistryKey::SetValueKey method](nf-portcls-iregistrykey-setvaluekey.md) | The SetValueKey method replaces or creates a value entry under the open key. |
| [PcRegisterAdapterPowerManagement function](nf-portcls-pcregisteradapterpowermanagement.md) | The PcRegisterAdapterPowerManagement function registers the adapter's power-management interface with the PortCls system driver. |
| [PcGetContentRights function](nf-portcls-pcgetcontentrights.md) | The PcGetContentRights function retrieves the DRM content rights assigned to a DRM content ID. Note that this function call is identical in operation to the DrmGetContentRights function, and its parameter definitions and return value are also identical. |
| [PcRemoveStreamResource function](nf-portcls-pcremovestreamresource.md) | PcRemoveStreamResource removes an existing stream resource. |
| [IMiniportWaveCyclicStream::GetPosition method](nf-portcls-iminiportwavecyclicstream-getposition.md) | The GetPosition method gets the current position of the stream. |
| [IMiniportWavePciStream::GetPosition method](nf-portcls-iminiportwavepcistream-getposition.md) | The GetPosition method gets the current position of the stream. |
| [PcAddStreamResource function](nf-portcls-pcaddstreamresource.md) | PcAddStreamResource adds a stream resource. |
| [IServiceGroup::RequestService method](nf-portcls-iservicegroup-requestservice~r1.md) | TBD |
| [IMiniportWavePciStream::GetAllocatorFraming method](nf-portcls-iminiportwavepcistream-getallocatorframing.md) | The GetAllocatorFraming method gets the preferred allocator-framing parameters for the stream. |
| [AddBusNumberFromParent function](nf-portcls-addbusnumberfromparent.md) | TBD |
| [IInterruptSync::GetKInterrupt method](nf-portcls-iinterruptsync-getkinterrupt.md) | The GetKInterrupt method gets a WDM interrupt object from a port-class synchronization object. |
| [FindUntranslatedSubAllocateFrom function](nf-portcls-finduntranslatedsuballocatefrom.md) | TBD |
| [IMiniportStreamAudioEngineNode::GetStreamChannelVolume method](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelvolume.md) | Gets the current volume level that is applied to the audio stream. |
| [IUnregisterPhysicalConnection::UnregisterPhysicalConnectionFromExternal method](nf-portcls-iunregisterphysicalconnection-unregisterphysicalconnectionfromexternal.md) | The UnregisterPhysicalConnectionFromExternal method deletes the registration of a physical connection that was registered by a previous call to PcRegisterPhysicalConnectionFromExternal. |
| [FindUntranslatedDeviceSpecific function](nf-portcls-finduntranslateddevicespecific.md) | TBD |
| [IMiniportWavePciStream::SetState method](nf-portcls-iminiportwavepcistream-setstate.md) | The SetState method changes the state of the stream transport. |
| [PcRegisterIoTimeout function](nf-portcls-pcregisteriotimeout.md) | The PcRegisterIoTimeout function registers a driver-supplied I/O-timer callback routine for a specified device object. |
| [IMiniportMidi::Init method](nf-portcls-iminiportmidi-init.md) | The Init method initializes the MIDI miniport object. |
| [IPortWaveRTStream::GetPhysicalPageAddress method](nf-portcls-iportwavertstream-getphysicalpageaddress.md) | The GetPhysicalPageAddress method returns the physical address for a page within a memory descriptor list (MDL). |
| [IMiniportWaveRT::NewStream method](nf-portcls-iminiportwavert-newstream~r3.md) | TBD |
| [IPinName::GetPinName method](nf-portcls-ipinname-getpinname.md) | The GetPinName method retrieves the friendly name of an audio endpoint. |
| [PcRegisterSubdevice function](nf-portcls-pcregistersubdevice.md) | The PcRegisterSubdevice function registers a subdevice to make it available for use by clients. |
| [IPortClsPower::RegisterAdapterPowerManagement method](nf-portcls-iportclspower-registeradapterpowermanagement.md) | The RegisterAdapterPowerManagement method registers the power management interface of the adapter with PortCls. |
| [FindTranslatedDma function](nf-portcls-findtranslateddma.md) | TBD |
| [IRegistryKey::EnumerateValueKey method](nf-portcls-iregistrykey-enumeratevaluekey.md) | The EnumerateValueKey method returns information about a registry entry that contains a value key. |
| [IMiniportWaveCyclicStream::NormalizePhysicalPosition method](nf-portcls-iminiportwavecyclicstream-normalizephysicalposition.md) | The NormalizePhysicalPosition method converts a physical buffer position to a time-based value. |
| [IMiniportAudioEngineNode::SetDeviceChannelMute method](nf-portcls-iminiportaudioenginenode-setdevicechannelmute.md) | Sets the state of the Mute node for the audio device channel. |
| [IMiniportWavePci::Service method](nf-portcls-iminiportwavepci-service~r2.md) | TBD |
| [PcAddContentHandlers function](nf-portcls-pcaddcontenthandlers.md) | The PcAddContentHandlers function provides the system with a list of functions that handle protected content. |
| [IMiniportAudioEngineNode::GetDeviceChannelPeakMeter method](nf-portcls-iminiportaudioenginenode-getdevicechannelpeakmeter.md) | Gets the PeakMeter value for the audio device channel. |
| [PcGetPhysicalDeviceObject function](nf-portcls-pcgetphysicaldeviceobject.md) | The PcGetPhysicalDeviceObject function enables audio miniport drivers to retrieve the underlying physical device object of the audio device. |
| [IMiniportMidi::NewStream method](nf-portcls-iminiportmidi-newstream.md) | The NewStream method creates a new instance of a logical stream associated with a specified physical channel. |
| [PcAssignPowerFrameworkSettings function](nf-portcls-pcassignpowerframeworksettings.md) | TBD |
| [IMiniportWavePciStream::Service method](nf-portcls-iminiportwavepcistream-service~r1.md) | TBD |
| [DEFINE_PCAUTOMATION_TABLE_PROP function](nf-portcls-define-pcautomation-table-prop.md) | TBD |
| [IPortWaveRTStream::UnmapAllocatedPages method](nf-portcls-iportwavertstream-unmapallocatedpages.md) | The UnmapAllocatedPages method releases a mapping. |
| [IPreFetchOffset::SetPreFetchOffset method](nf-portcls-iprefetchoffset-setprefetchoffset.md) | The SetPreFetchOffset method sets the prefetch offset, which is the number of bytes of data separating the write cursor from the play cursor in a DirectSound output stream. |
| [GTI_MICROSECONDS function](nf-portcls-gti-microseconds.md) | TBD |
| [WIN95COMPAT_ReadPortUShort function](nf-portcls-win95compat-readportushort.md) | TBD |
| [IRegistryKey::NewSubKey method](nf-portcls-iregistrykey-newsubkey.md) | The NewSubKey method either creates a new registry subkey or opens an existing subkey under the key represented by the IRegistryKey object. |
| [IPortWaveRTStream::AllocatePagesForMdl method](nf-portcls-iportwavertstream-allocatepagesformdl.md) | The AllocatePagesForMdl method allocates a list of nonpaged physical memory pages and returns a pointer to a memory descriptor list (MDL) that describes them. |
| [IMiniportWaveRTOutputStream::SetWritePacket method](nf-portcls-iminiportwavertoutputstream-setwritepacket.md) | SetWritePacket informs the driver that the OS has written valid data to the WaveRT buffer. |
| [IMiniportWaveCyclicStream::SetNotificationFreq method](nf-portcls-iminiportwavecyclicstream-setnotificationfreq.md) | The SetNotificationFreq method controls the frequency at which notification interrupts are generated by setting the interval between successive interrupts. |
| [IServiceGroup::AddMember method](nf-portcls-iservicegroup-addmember.md) | The AddMember method adds a member to the service group. |
| [IMiniportTopology::Init method](nf-portcls-iminiporttopology-init.md) | The Init method initializes the topology miniport object. |
| [IMiniportWaveCyclicStream::Silence method](nf-portcls-iminiportwavecyclicstream-silence.md) | The Silence method is used to copy silence samples to a specified buffer. |
| [IRegistryKey::QueryValueKey method](nf-portcls-iregistrykey-queryvaluekey.md) | The QueryValueKey method retrieves information about a registry key's value entries, including their names, types, data sizes, and values. |
| [IMiniportWavePciStream::Service method](nf-portcls-iminiportwavepcistream-service.md) | The Service method notifies the miniport driver of a request for service. |
| [PCSTREAMRESOURCE_DESCRIPTOR_INIT function](nf-portcls-pcstreamresource-descriptor-init.md) | TBD |
| [IMiniportWavePciStream::GetPosition method](nf-portcls-iminiportwavepcistream-getposition~r1.md) | TBD |
| [IServiceGroup::CancelDelayedService method](nf-portcls-iservicegroup-canceldelayedservice.md) | The CancelDelayedService method cancels the previously requested delayed service. |
| [AddAssignedResourceFromParent function](nf-portcls-addassignedresourcefromparent.md) | TBD |
| [IResourceList::NumberOfEntries method](nf-portcls-iresourcelist-numberofentries.md) | The NumberOfEntries method returns the number of resource items in the resource list. |
| [IPortClsNotifications::AllocNotificationBuffer method](nf-portcls-iportclsnotifications-allocnotificationbuffer.md) | Allocates a buffer of the specified size, in the specified memory pool, for use in sending notifications, to allow for communications between audio modules and UWP apps. |
| [PcForwardContentToFileObject function](nf-portcls-pcforwardcontenttofileobject.md) | The PcForwardContentToFileObject function is obsolete and is maintained only to support existing drivers. |
| [IMiniportStreamAudioEngineNode::SetStreamCurrentWritePosition method](nf-portcls-iminiportstreamaudioenginenode-setstreamcurrentwriteposition.md) | Sets the current cursor position in the audio data stream that is being captured from the endpoint. |
| [IRegistryKey::QueryKey method](nf-portcls-iregistrykey-querykey.md) | The QueryKey method retrieves information about a registry key, including the key name, key class, and the number of subkeys and their sizes. |
| [PcNewInterruptSync function](nf-portcls-pcnewinterruptsync.md) | The PcNewInterruptSync function creates and initializes an interrupt-synchronization object. |
| [IMiniportAudioEngineNode::SetDeviceFormat method](nf-portcls-iminiportaudioenginenode-setdeviceformat.md) | Sets the audio data format for an audio device. |
| [IMiniportWaveCyclicStream::SetFormat method](nf-portcls-iminiportwavecyclicstream-setformat~r1.md) | TBD |
| [WIN95COMPAT_WritePortUChar function](nf-portcls-win95compat-writeportuchar.md) | TBD |
| [IResourceList::UntranslatedList method](nf-portcls-iresourcelist-untranslatedlist.md) | The UntranslatedList method returns the list of untranslated resources. |
| [IMiniportWaveRT::NewStream method](nf-portcls-iminiportwavert-newstream.md) | The NewStream method creates a new instance of a WaveRT stream object. |
| [IMiniportAudioEngineNode::SetGfxState method](nf-portcls-iminiportaudioenginenode-setgfxstate.md) | TBD |
| [IMiniportWaveCyclic::NewStream method](nf-portcls-iminiportwavecyclic-newstream.md) | The NewStream method creates a new instance of a logical stream that is associated with a specified physical channel. |
| [AddMemoryFromParent function](nf-portcls-addmemoryfromparent.md) | TBD |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IPortClsEtwHelper interface](nn-portcls-iportclsetwhelper.md) | The IPortClsEtwHelper interface allows an audio miniport driver to access the Event Tracing for Windows (ETW) helper functions. |
| [IMiniportPnpNotify interface](nn-portcls-iminiportpnpnotify.md) | TBD |
| [IMusicTechnology interface](nn-portcls-imusictechnology.md) | TBD |
| [IRegistryKey interface](nn-portcls-iregistrykey.md) | TBD |
| [IMiniportAudioEngineNode interface](nn-portcls-iminiportaudioenginenode.md) | This interface allows a miniport driver to use KS properties that access the audio engine via a KS filter handle. |
| [IPortWaveCyclic interface](nn-portcls-iportwavecyclic.md) | TBD |
| [IPortClsSubdeviceEx interface](nn-portcls-iportclssubdeviceex.md) | TBD |
| [IPortMidi interface](nn-portcls-iportmidi.md) | TBD |
| [IDmaChannel interface](nn-portcls-idmachannel.md) | TBD |
| [IMiniportWavePci interface](nn-portcls-iminiportwavepci.md) | TBD |
| [IPortWaveRTStream interface](nn-portcls-iportwavertstream.md) | TBD |
| [IDmaChannelSlave interface](nn-portcls-idmachannelslave.md) | TBD |
| [IPortWaveRT interface](nn-portcls-iportwavert.md) | TBD |
| [IPowerNotify interface](nn-portcls-ipowernotify.md) | TBD |
| [IServiceGroup interface](nn-portcls-iservicegroup.md) | TBD |
| [IMiniportTopology interface](nn-portcls-iminiporttopology.md) | TBD |
| [IPortClsStreamResourceManager2 interface](nn-portcls-iportclsstreamresourcemanager2.md) | TBD |
| [IServiceSink interface](nn-portcls-iservicesink.md) | TBD |
| [IPortEvents interface](nn-portcls-iportevents.md) | TBD |
| [IPortClsPnp interface](nn-portcls-iportclspnp.md) | TBD |
| [IAdapterPowerManagement3 interface](nn-portcls-iadapterpowermanagement3.md) | The IAdapterPowerManagement3 interface inherits from IUnknown, and it is used for receiving power management messages. |
| [IAdapterPowerManagement2 interface](nn-portcls-iadapterpowermanagement2.md) | TBD |
| [IInterruptSync interface](nn-portcls-iinterruptsync.md) | TBD |
| [IPortClsStreamResourceManager interface](nn-portcls-iportclsstreamresourcemanager.md) | TBD |
| [IMiniportWaveRTStream interface](nn-portcls-iminiportwavertstream.md) | TBD |
| [IPortClsPower interface](nn-portcls-iportclspower.md) | TBD |
| [IPort interface](nn-portcls-iport.md) | TBD |
| [IMiniportWaveCyclicStream interface](nn-portcls-iminiportwavecyclicstream.md) | TBD |
| [IPortWavePci interface](nn-portcls-iportwavepci.md) | TBD |
| [IMiniportWaveRTInputStream interface](nn-portcls-iminiportwavertinputstream.md) | TBD |
| [IResourceList interface](nn-portcls-iresourcelist.md) | TBD |
| [IAdapterPowerManagement interface](nn-portcls-iadapterpowermanagement.md) | TBD |
| [IPinCount interface](nn-portcls-ipincount.md) | TBD |
| [IMiniportWaveRTStreamNotification interface](nn-portcls-iminiportwavertstreamnotification.md) | TBD |
| [IPinName interface](nn-portcls-ipinname.md) | TBD |
| [IMiniportMidi interface](nn-portcls-iminiportmidi.md) | TBD |
| [IMiniportWavePciStream interface](nn-portcls-iminiportwavepcistream.md) | TBD |
| [IMiniport interface](nn-portcls-iminiport.md) | TBD |
| [IMiniportWaveRTOutputStream interface](nn-portcls-iminiportwavertoutputstream.md) | TBD |
| [IUnregisterPhysicalConnection interface](nn-portcls-iunregisterphysicalconnection.md) | TBD |
| [IPortClsRuntimePower interface](nn-portcls-iportclsruntimepower.md) | TBD |
| [IPortTopology interface](nn-portcls-iporttopology.md) | TBD |
| [IMiniportAudioSignalProcessing interface](nn-portcls-iminiportaudiosignalprocessing.md) | The IMiniportAudioSignalProcessing interface is implemented by the WaveRT miniport component of any audio driver, if any of its pins support audio signal processing modes. |
| [IMiniportMidiStream interface](nn-portcls-iminiportmidistream.md) | TBD |
| [IAdapterPnpManagement interface](nn-portcls-iadapterpnpmanagement.md) | TBD |
| [IPortWMIRegistration interface](nn-portcls-iportwmiregistration.md) | TBD |
| [IMiniportStreamAudioEngineNode2 interface](nn-portcls-iminiportstreamaudioenginenode2.md) | The IMiniportStreamAudioEngineNode2 interface allows an audio miniport driver to extend the capabilities of the IMiniportStreamAudioEngineNode interface. |
| [IPortClsVersion interface](nn-portcls-iportclsversion.md) | TBD |
| [IPortWavePciStream interface](nn-portcls-iportwavepcistream.md) | TBD |
| [IPreFetchOffset interface](nn-portcls-iprefetchoffset.md) | TBD |
| [IMiniportStreamAudioEngineNode interface](nn-portcls-iminiportstreamaudioenginenode.md) | This interface allows a miniport driver to use KS properties that access the audio engine via a pin instance handle. |
| [IDrmPort interface](nn-portcls-idrmport.md) | TBD |
| [IDrmPort2 interface](nn-portcls-idrmport2.md) | TBD |
| [IPortClsNotifications interface](nn-portcls-iportclsnotifications.md) | TBD |
| [IUnregisterSubdevice interface](nn-portcls-iunregistersubdevice.md) | TBD |
| [IMiniportWaveCyclic interface](nn-portcls-iminiportwavecyclic.md) | TBD |
| [IMiniportWaveRT interface](nn-portcls-iminiportwavert.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PCPROPERTY_REQUEST structure](ns-portcls--pcproperty-request~r1.md) | TBD |
| [unnamed_struct_0c40_5 structure](ns-portcls---unnamed-struct-0c40-5.md) | TBD |
| [unnamed_struct_0c40_4 structure](ns-portcls---unnamed-struct-0c40-4.md) | TBD |
| [unnamed_struct_0c40_6 structure](ns-portcls---unnamed-struct-0c40-6.md) | TBD |
| [PCSTREAMRESOURCE_DESCRIPTOR structure](ns-portcls--pcstreamresource-descriptor.md) | PCSTREAMRESOURCE_DESCRIPTOR defines the stream resource. Use PCSTREAMRESOURCE_DESCRIPTOR_INIT to correctly initialize this structure. |
| [PCEVENT_REQUEST structure](ns-portcls--pcevent-request.md) | TBD |
| [unnamed_struct_0c40_8 structure](ns-portcls---unnamed-struct-0c40-8.md) | TBD |
| [PC_POWER_FRAMEWORK_SETTINGS structure](ns-portcls--pc-power-framework-settings.md) | TBD |
| [PCMETHOD_REQUEST structure](ns-portcls--pcmethod-request~r1.md) | TBD |
| [PCEVENT_REQUEST structure](ns-portcls--pcevent-request~r1.md) | TBD |
| [PCMETHOD_REQUEST structure](ns-portcls--pcmethod-request.md) | TBD |
| [unnamed_struct_0c40_9 structure](ns-portcls---unnamed-struct-0c40-9.md) | TBD |
| [PCPROPERTY_REQUEST structure](ns-portcls--pcproperty-request.md) | TBD |
| [unnamed_struct_0c40_7 structure](ns-portcls---unnamed-struct-0c40-7.md) | TBD |
| [unnamed_struct_0c40_3 structure](ns-portcls---unnamed-struct-0c40-3.md) | TBD |
| [PCNOTIFICATION_BUFFER structure](ns-portcls--pcnotification-buffer.md) | The notification buffer used by IPortClsNotifications. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [PC_REBALANCE_TYPE enumeration](ne-portcls-pc-rebalance-type.md) | The PC_REBALANCE_TYPE enum describes the type of support for rebalancing. |
| [EPcMiniportEngineEvent enumeration](ne-portcls-epcminiportengineevent.md) | This topic introduces the EPcMiniportEngineEvent enum, and describes the parameters that provide additional information when the miniport driver reports a glitching error. |
| [eEngineFormatType enumeration](ne-portcls-eengineformattype.md) | The eEngineFormatType enumeration defines constants that specify the audio data type supported by the audio engine. |
| [unnamed_enum_0c40_11 enumeration](ne-portcls---unnamed-enum-0c40-11.md) | TBD |
| [unnamed_enum_0c40_14 enumeration](ne-portcls---unnamed-enum-0c40-14.md) | TBD |
| [PcStreamResourceType enumeration](ne-portcls--pcstreamresourcetype.md) | This topic discusses the PcStreamResourceType enum, and describes its members. The PcStreamResourceType enum is used to define the type of resources used for specific audio streaming. |
| [INTERRUPTSYNCMODE enumeration](ne-portcls-interruptsyncmode.md) | TBD |
| [PC_EXIT_LATENCY enumeration](ne-portcls--pc-exit-latency.md) | This topic discusses the PC_EXIT_LATENCY enum, and describes its members. The latency times map to specific maximum times in which the device must be able to exit its sleep state and enter the fully functional state (D0). |
| [eChannelTargetType enumeration](ne-portcls-echanneltargettype.md) | The eChannelTargetType enumeration defines constants that specify a type of node (target) in a given channel. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_PC_POST_PO_FX_REGISTER_DEVICE callback function](nc-portcls-evt-pc-post-po-fx-register-device.md) | TBD |
| [PCPFNEVENT_HANDLER callback](nc-portcls-pcpfnevent-handler.md) | An EventHandler routine processes event requests. |
| [PCPFNMETHOD_HANDLER callback function](nc-portcls-pcpfnmethod-handler.md) | TBD |
| [PCPFNIRPHANDLER callback function](nc-portcls-pcpfnirphandler.md) | TBD |
| [EVT_PC_PRE_PO_FX_UNREGISTER_DEVICE callback function](nc-portcls-evt-pc-pre-po-fx-unregister-device.md) | TBD |
| [PINTERRUPTSYNCROUTINE callback function](nc-portcls-pinterruptsyncroutine.md) | TBD |
| [DISPATCH_LEVEL callback function](nc-portcls-dispatch-level.md) | TBD |
| [PCPFNSTARTDEVICE callback function](nc-portcls-pcpfnstartdevice.md) | TBD |
| [PCPFNPROPERTY_HANDLER callback function](nc-portcls-pcpfnproperty-handler.md) | TBD |

This header is used in these topics:

- [audio](..content/_audio)
