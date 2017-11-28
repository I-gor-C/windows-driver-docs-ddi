# Pepfx.h header


This header is used by unknown technology.

Pepfx.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function](nf-pepfx-pep-acpi-initialize-extended-io-resource.md) | The PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_EXTENDED_ADDRESS structure. |
| [PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function](nf-pepfx-pep-acpi-initialize-extended-memory-resource.md) | The PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_EXTENDED_ADDRESS structure. |
| [PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE function](nf-pepfx-pep-acpi-initialize-gpio-int-resource.md) | The PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_GPIO_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_GPIO_IO_RESOURCE function](nf-pepfx-pep-acpi-initialize-gpio-io-resource.md) | The PEP_ACPI_INITIALIZE_GPIO_IO_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_GPIO_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE function](nf-pepfx-pep-acpi-initialize-interrupt-resource.md) | The PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_INTERRUPT_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_IOPORT_RESOURCE function](nf-pepfx-pep-acpi-initialize-ioport-resource.md) | The PEP_ACPI_INITIALIZE_IOPORT_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_IO_MEMORY_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function](nf-pepfx-pep-acpi-initialize-memory-resource.md) | The PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_IO_MEMORY_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE function](nf-pepfx-pep-acpi-initialize-spb-i2c-resource.md) | The PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_I2C_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE function](nf-pepfx-pep-acpi-initialize-spb-spi-resource.md) | The PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_SPI_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE function](nf-pepfx-pep-acpi-initialize-spb-uart-resource.md) | The PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_UART_RESOURCE structure. |
| [PoFxRegisterCoreDevice function](nf-pepfx-pofxregistercoredevice.md) | The PoFxRegisterCoreDevice routine registers a new core system resource with the Windows power management framework (PoFx). |
| [PoFxRegisterPlugin function](nf-pepfx-pofxregisterplugin.md) | The PoFxRegisterPlugin routine registers a platform extension plug-in (PEP) with the Windows power management framework (PoFx). |
| [PoFxRegisterPluginEx function](nf-pepfx-pofxregisterpluginex.md) | The PoFxRegisterPluginEx routine registers a platform extension plug-in (PEP) with the Windows power management framework (PoFx). |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PEPCALLBACKNOTIFYACPI callback](nc-pepfx-pepcallbacknotifyacpi.md) | An AcceptAcpiNotification event callback routine handles ACPI notifications from the Windows power management framework (PoFx). |
| [PEPCALLBACKNOTIFYDPM callback](nc-pepfx-pepcallbacknotifydpm.md) | An AcceptDeviceNotification event callback routine handles device power management (DPM) notifications from the Windows power management framework (PoFx). |
| [PEPCALLBACKNOTIFYPPM callback](nc-pepfx-pepcallbacknotifyppm.md) | An AcceptProcessorNotification event callback routine handles processor power management (PPM) notifications from the Windows power management framework (PoFx). |
| [PEPCALLBACKPOWERONCRASHDUMPDEVICE callback](nc-pepfx-pepcallbackpoweroncrashdumpdevice.md) | The PowerOnDumpDeviceCallback callback routine turns on the crash-dump device. |
| [POFXCALLBACKREQUESTCOMMON callback](nc-pepfx-pofxcallbackrequestcommon.md) | The RequestCommon routine is a generic request handler. |
| [PPO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK callback](nc-pepfx-ppo-enumerate-interrupt-source-callback.md) | An EnumerateInterruptSource callback routine supplies a platform extension plug-in (PEP) with information about an interrupt source. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [PEP_ABANDON_DEVICE structure](ns-pepfx--pep-abandon-device.md) | The PEP_ABANDON_DEVICE structure identifies a device that has been abandoned and will no longer be used by the operating system. |
| [PEP_ACPI_ABANDON_DEVICE structure](ns-pepfx--pep-acpi-abandon-device.md) | The PEP_ACPI_ABANDON_DEVICE structure indicates whether the platform extension plug-in (PEP) accepts ownership of an abandoned device. |
| [PEP_ACPI_ENUMERATE_DEVICE_NAMESPACE structure](ns-pepfx--pep-acpi-enumerate-device-namespace.md) | The PEP_ACPI_ENUMERATE_DEVICE_NAMESPACE structure contains an enumeration of the objects in the namespace of the device. |
| [PEP_ACPI_EVALUATE_CONTROL_METHOD structure](ns-pepfx--pep-acpi-evaluate-control-method.md) | The PEP_ACPI_EVALUATE_CONTROL_METHOD structure specifies an ACPI control method to evaluate, an input argument to supply to this method, and an output buffer for the result of the evaluation. |
| [PEP_ACPI_EXTENDED_ADDRESS structure](ns-pepfx--pep-acpi-extended-address.md) | The PEP_ACPI_EXTENDED_ADDRESS structure is used to report resource usage in the address space such as memory and IO. |
| [PEP_ACPI_GPIO_RESOURCE structure](ns-pepfx--pep-acpi-gpio-resource.md) | The PEP_ACPI_GPIO_RESOURCE structure describes the ACPI configuration for a general purpose input/output (GPIO) resource. |
| [PEP_ACPI_INTERRUPT_RESOURCE structure](ns-pepfx--pep-acpi-interrupt-resource.md) | The PEP_ACPI_INTERRUPT_RESOURCE structure describes an ACPI interrupt resource. |
| [PEP_ACPI_IO_MEMORY_RESOURCE structure](ns-pepfx--pep-acpi-io-memory-resource.md) | The PEP_ACPI_IO_MEMORY_RESOURCE structure describes an ACPI IO port descriptor resource. |
| [PEP_ACPI_OBJECT_NAME structure](ns-pepfx--pep-acpi-object-name.md) | The PEP_ACPI_OBJECT_NAME union contains the four-character name of an ACPI object. |
| [PEP_ACPI_OBJECT_NAME_WITH_TYPE structure](ns-pepfx--pep-acpi-object-name-with-type.md) | The PEP_ACPI_OBJECT_NAME_WITH_TYPE structure that specifies both the path-relative name of an ACPI object and the type of this object. |
| [PEP_ACPI_PREPARE_DEVICE structure](ns-pepfx--pep-acpi-prepare-device.md) | The PEP_ACPI_PREPARE_DEVICE structure indicates whether a platform extension plug-in (PEP) is prepared to provide ACPI services for the specified device. |
| [PEP_ACPI_QUERY_DEVICE_CONTROL_RESOURCES structure](ns-pepfx--pep-acpi-query-device-control-resources.md) | The PEP_ACPI_QUERY_DEVICE_CONTROL_RESOURCES structure contains a list of raw resources that are needed to control power to the device. |
| [PEP_ACPI_QUERY_OBJECT_INFORMATION structure](ns-pepfx--pep-acpi-query-object-information.md) | The PEP_ACPI_QUERY_OBJECT_INFORMATION structure contains information about an ACPI object. |
| [PEP_ACPI_REGISTER_DEVICE structure](ns-pepfx--pep-acpi-register-device.md) | The PEP_ACPI_REGISTER_DEVICE structure contains registration information about a device for which the platform extension plug-in (PEP) is to provide ACPI services. |
| [PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES structure](ns-pepfx--pep-acpi-request-convert-to-bios-resources.md) | The PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES structure is used in the process of converting ACPI resources to BIOS resources by one of the PEP initialization functions. |
| [PEP_ACPI_RESOURCE structure](ns-pepfx--pep-acpi-resource.md) | The PEP_ACPI_RESOURCE structure contains hardware details for a specific ACPI resource. |
| [PEP_ACPI_RESOURCE_FLAGS structure](ns-pepfx--pep-acpi-resource-flags.md) | The PEP_ACPI_RESOURCE_FLAGS structure contains flags describing an ACPI resource. |
| [PEP_ACPI_SPB_I2C_RESOURCE structure](ns-pepfx--pep-acpi-spb-i2c-resource.md) | The PEP_ACPI_SPB_I2C_RESOURCE structure describes an ACPI I2C serial bus resource. |
| [PEP_ACPI_SPB_RESOURCE structure](ns-pepfx--pep-acpi-spb-resource.md) | The PEP_ACPI_SPB_RESOURCE structure describes an ACPI serial bus connection resource. |
| [PEP_ACPI_SPB_SPI_RESOURCE structure](ns-pepfx--pep-acpi-spb-spi-resource.md) | The PEP_ACPI_SPB_SPI_RESOURCE structure describes an ACPI SPI serial bus resource. |
| [PEP_ACPI_SPB_UART_RESOURCE structure](ns-pepfx--pep-acpi-spb-uart-resource.md) | The PEP_ACPI_SPB_UART_RESOURCE structure describes an ACPI UART serial bus resource. |
| [PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES structure](ns-pepfx--pep-acpi-translated-device-control-resources.md) | The PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES structure contains a list of translated power-control resources for the platform extension plug-in (PEP) to use. |
| [PEP_ACPI_UNREGISTER_DEVICE structure](ns-pepfx--pep-acpi-unregister-device.md) | The PEP_ACPI_UNREGISTER_DEVICE structure contains information about a device that has been unregistered from ACPI services. |
| [PEP_COMPONENT_PERF_INFO structure](ns-pepfx--pep-component-perf-info.md) | The PEP_COMPONENT_PERF_INFO structure describes the performance states (P-states) of a component. |
| [PEP_COMPONENT_PERF_SET structure](ns-pepfx--pep-component-perf-set.md) | The PEP_COMPONENT_PERF_SET structure describes the performance states (P-states) in a P-state set. |
| [PEP_COMPONENT_PERF_STATE_REQUEST structure](ns-pepfx--pep-component-perf-state-request.md) | The PEP_COMPONENT_PERF_STATE_REQUEST structure specifies a performance state (P-state) set and a new performance level to assign to this set. |
| [PEP_COMPONENT_PLATFORM_CONSTRAINTS structure](ns-pepfx--pep-component-platform-constraints.md) | The PEP_COMPONENT_PLATFORM_CONSTRAINTS structure describes the lowest-powered Fx state of that a component can be in when the platform is in a particular idle state. |
| [PEP_COMPONENT_V2 structure](ns-pepfx--pep-component-v2.md) | The PEP_COMPONENT_V2 structure specifies the power state attributes of a component in the device. |
| [PEP_COORDINATED_DEPENDENCY_OPTION structure](ns-pepfx--pep-coordinated-dependency-option.md) | The PEP_COORIDNATED_DEPENDENCY_OPTION structure describes a coordinated idle stateâ€™s dependency to the OS. |
| [PEP_COORDINATED_IDLE_STATE structure](ns-pepfx--pep-coordinated-idle-state.md) | The PEP_COORIDNATED_IDLE_STATE structure describes a coordinated idle state to the OS. |
| [PEP_CRASHDUMP_INFORMATION structure](ns-pepfx--pep-crashdump-information.md) | The PEP_CRASHDUMP_INFORMATION structure contains information about a crash-dump device. |
| [PEP_DEBUGGER_TRANSITION_REQUIREMENTS structure](ns-pepfx--pep-debugger-transition-requirements.md) | The PEP_DEBUGGER_TRANSITION_REQUIREMENTS structure indicates the platform idle states for which the debugger device must be turned on. |
| [PEP_DEVICE_PLATFORM_CONSTRAINTS structure](ns-pepfx--pep-device-platform-constraints.md) | The PEP_DEVICE_PLATFORM_CONSTRAINTS structure specifies the constraints for entry to the various Dx power states that are supported by a device. |
| [PEP_DEVICE_POWER_STATE structure](ns-pepfx--pep-device-power-state.md) | The PEP_DEVICE_POWER_STATE structure indicates the status of a transition to a new Dx (device power) state. |
| [PEP_DEVICE_REGISTER_V2 structure](ns-pepfx--pep-device-register-v2.md) | The PEP_DEVICE_REGISTER structure describes all the components in a particular device. |
| [PEP_DEVICE_STARTED structure](ns-pepfx--pep-device-started.md) | The PEP_DEVICE_STARTED structure identifies a device whose driver has completed its registration with the Windows power management framework (PoFx). |
| [PEP_INFORMATION structure](ns-pepfx--pep-information.md) | The PEP_INFORMATION structure specifies the interface that the platform extension plug-in (PEP) uses to receive notifications from the Windows power management framework (PoFx). |
| [PEP_KERNEL_INFORMATION_STRUCT_V3 structure](ns-pepfx--pep-kernel-information-struct-v3.md) | The PEP_KERNEL_INFORMATION_STRUCT_V3 structure specifies the interface that the power extension plug-in (PEP) uses to request services from the Windows power management framework (PoFx). |
| [PEP_LOW_POWER_EPOCH structure](ns-pepfx--pep-low-power-epoch.md) | The PEP_LOW_POWER_EPOCH structure is used to provide data for a PEP_DPM_LOW_POWER_EPOCH notification (deprecated). |
| [PEP_NOTIFY_COMPONENT_IDLE_STATE structure](ns-pepfx--pep-notify-component-idle-state.md) | The PEP_NOTIFY_COMPONENT_IDLE_STATE structure contains status information about a component's pending transition to a new Fx power state. |
| [PEP_PERF_STATE structure](ns-pepfx--pep-perf-state.md) | The PEP_PERF_STATE structure describes a performance state (P-state) in a P-state set in which the P-states are specified as a list of one or more discrete values. |
| [PEP_PLATFORM_IDLE_STATE structure](ns-pepfx--pep-platform-idle-state.md) | The PEP_PLATFORM_IDLE_STATE structure specifies the properties of a platform idle state. |
| [PEP_PLATFORM_IDLE_STATE_UPDATE structure](ns-pepfx--pep-platform-idle-state-update.md) | The PEP_PLATFORM_IDLE_STATE_UPDATE structure contains the updated properties of a platform idle state. |
| [PEP_POWER_CONTROL_COMPLETE structure](ns-pepfx--pep-power-control-complete.md) | The PEP_POWER_CONTROL_COMPLETE structure contains status information for a power control operation that the PEP previously requested and that the device driver has completed. |
| [PEP_POWER_CONTROL_REQUEST structure](ns-pepfx--pep-power-control-request.md) | The PEP_POWER_CONTROL_REQUEST structure contains a request from a driver for a power control operation. |
| [PEP_PPM_CONTEXT_QUERY_PARKING_PAGE structure](ns-pepfx--pep-ppm-context-query-parking-page.md) | The PEP_PPM_CONTEXT_QUERY_PARKING_PAGE structure describes the parking page for a processor. |
| [PEP_PPM_CST_STATE structure](ns-pepfx--pep-ppm-cst-state.md) | The PEP_PPM_CST_STATE structure specifies the properties of a C state (ACPI processor power state). |
| [PEP_PPM_CST_STATES structure](ns-pepfx--pep-ppm-cst-states.md) | The PEP_PPM_CST_STATES structure specifies the properties of the C states (ACPI processor power states) that are supported for a processor. |
| [PEP_PPM_ENTER_SYSTEM_STATE structure](ns-pepfx--pep-ppm-enter-system-state.md) | Used in the PEP_NOTIFY_PPM_ENTER_SYSTEM_STATE notification to notify PEP that the system is about to enter a system power state.  . |
| [PEP_PPM_FEEDBACK_READ structure](ns-pepfx--pep-ppm-feedback-read.md) | The PEP_PPM_FEEDBACK_READ structure contains the value read from a processor performance feedback counter. |
| [PEP_PPM_IDLE_COMPLETE structure](ns-pepfx--pep-ppm-idle-complete.md) | The PEP_PPM_IDLE_COMPLETE structure describe the idle states from which the processor and hardware platform are waking. |
| [PEP_PPM_IDLE_COMPLETE_V2 structure](ns-pepfx--pep-ppm-idle-complete-v2.md) | The PEP_PPM_IDLE_COMPLETE_V2 structure describe the idle states from which the processor and hardware platform are waking. |
| [PEP_PPM_IDLE_EXECUTE structure](ns-pepfx--pep-ppm-idle-execute.md) | The PEP_PPM_IDLE_EXECUTE structure specifies the idle state that the processor is to enter. |
| [PEP_PPM_IDLE_EXECUTE_V2 structure](ns-pepfx--pep-ppm-idle-execute-v2.md) | The PEP_PPM_IDLE_EXECUTE_V2 structure specifies the idle state that the processor is to enter. |
| [PEP_PPM_INITIATE_WAKE structure](ns-pepfx--pep-ppm-initiate-wake.md) | The PEP_PPM_INITIATE_WAKE structure indicates whether a processor requires an interrupt to wake up from an idle state. |
| [PEP_PPM_IS_PROCESSOR_HALTED structure](ns-pepfx--pep-ppm-is-processor-halted.md) | The PEP_PPM_IS_PROCESSOR_HALTED structure indicates whether the processor is currently halted in its selected idle state. |
| [PEP_PPM_PARK_MASK structure](ns-pepfx--pep-ppm-park-mask.md) | The PEP_PROCESSOR_PARK_MASK structure contains the current core parking mask. |
| [PEP_PPM_PARK_SELECTION structure](ns-pepfx--pep-ppm-park-selection.md) | The PEP_PPM_PARK_SELECTION structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding which processors in the platform should be parked to reduce power consumption. |
| [PEP_PPM_PARK_SELECTION_V2 structure](ns-pepfx--pep-ppm-park-selection-v2.md) | The PEP_PPM_PARK_SELECTION_V2 structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding which processors in the platform should be parked to reduce power consumption. |
| [PEP_PPM_PERF_CHECK_COMPLETE structure](ns-pepfx--pep-ppm-perf-check-complete.md) | The PEP_PPM_PERF_CHECK_COMPLETE structure is used to inform the PEP of details regarding the completion of a periodic performance check evaluation. |
| [PEP_PPM_PERF_SET structure](ns-pepfx--pep-ppm-perf-set.md) | The PEP_PPM_PERF_SET structure specifies the new performance level that the operating system is requesting for the processor. |
| [PEP_PPM_PERF_SET_STATE structure](ns-pepfx--pep-ppm-perf-set-state.md) | Used in the PEP_NOTIFY_PPM_PERF_SET notification at runtime to set the current operating performance of the processor.  . |
| [PEP_PPM_PLATFORM_STATE_RESIDENCIES structure](ns-pepfx--pep-ppm-platform-state-residencies.md) | The PEP_PPM_PLATFORM_STATE_RESIDENCIES structure contains the accumulated residency times and transition counts for the idle states that are supported by the hardware platform. |
| [PEP_PPM_PLATFORM_STATE_RESIDENCY structure](ns-pepfx--pep-ppm-platform-state-residency.md) | The PEP_PPM_PLATFORM_STATE_RESIDENCY structure specifies the accumulated residency time and transition count for a particular platform idle state. |
| [PEP_PPM_QUERY_CAPABILITIES structure](ns-pepfx--pep-ppm-query-capabilities.md) | The PEP_PPM_QUERY_CAPABILITIES structure contains information about the processor power management (PPM) capabilities of the platform extension plug-in (PEP). |
| [PEP_PPM_QUERY_COORDINATED_DEPENDENCY structure](ns-pepfx--pep-ppm-query-coordinated-dependency.md) | The PEP_PPM_QUERY_COORDINATED_DEPENDENCY structure describes dependencies for coordinated idle states. |
| [PEP_PPM_QUERY_COORDINATED_STATES structure](ns-pepfx--pep-ppm-query-coordinated-states.md) | The PEP_PPM_QUERY_COORDINATED_STATES structure contains information about each coordinated idle state that the platform extension plug-in (PEP) supports. |
| [PEP_PPM_QUERY_DISCRETE_PERF_STATES structure](ns-pepfx--pep-ppm-query-discrete-perf-states.md) | Used in the PEP_NOTIFY_PPM_QUERY_DISCRETE_PERF_STATES notification that stores the list of discrete performance states that PEP supports, if the PEP_NOTIFY_PPM_QUERY_CAPABILITIES notification indicates support for discrete performance states. . |
| [PEP_PPM_QUERY_DOMAIN_INFO structure](ns-pepfx--pep-ppm-query-domain-info.md) | Used in the PEP_NOTIFY_PPM_QUERY_DOMAIN_INFO notification that queries for information about a performance domain. . |
| [PEP_PPM_QUERY_FEEDBACK_COUNTERS structure](ns-pepfx--pep-ppm-query-feedback-counters.md) | The PEP_PPM_QUERY_FEEDBACK_COUNTERS structure describes all the processor performance counters that the platform extension plug-in (PEP) supports for a particular processor. |
| [PEP_PPM_QUERY_IDLE_STATES_V2 structure](ns-pepfx--pep-ppm-query-idle-states-v2.md) | The PEP_PPM_QUERY_IDLE_STATES_V2 structure is used during processor initialization to query the platform extension plug-in (PEP) for a list of processor idle states that the processor supports. |
| [PEP_PPM_QUERY_PERF_CAPABILITIES structure](ns-pepfx--pep-ppm-query-perf-capabilities.md) | The PEP_PPM_QUERY_PERF_CAPABILITIES structure describes the performance capabilities of the processors in the specified processor performance domain. |
| [PEP_PPM_QUERY_PERF_CONSTRAINTS structure](ns-pepfx--pep-ppm-query-perf-constraints.md) | The PEP_PPM_PERF_CONSTRAINTS structure describes the performance limits to apply to the processor. |
| [PEP_PPM_QUERY_PLATFORM_STATE structure](ns-pepfx--pep-ppm-query-platform-state.md) | The PEP_PPM_QUERY_PLATFORM_STATE structure contains information about a platform idle state. |
| [PEP_PPM_QUERY_PLATFORM_STATES structure](ns-pepfx--pep-ppm-query-platform-states.md) | The PEP_PPM_QUERY_PLATFORM_STATES structure specifies the number of platform idle states the hardware platform supports. |
| [PEP_PPM_QUERY_STATE_NAME structure](ns-pepfx--pep-ppm-query-state-name.md) | The PEP_PPM_QUERY_STATE_NAME structure contains information about a specific coordinated or platform idle state. |
| [PEP_PPM_QUERY_VETO_REASON structure](ns-pepfx--pep-ppm-query-veto-reason.md) | The PEP_PPM_QUERY_VETO_REASON structure supplies a wide-character, null-terminated string that contains a descriptive, human-readable name for a veto reason. |
| [PEP_PPM_QUERY_VETO_REASONS structure](ns-pepfx--pep-ppm-query-veto-reasons.md) | The PEP_PPM_QUERY_VETO_REASONS structure specifies the total number of veto reasons that the PEP uses in calls to the ProcessorIdleVeto and PlatformIdleVeto routines. |
| [PEP_PPM_RESUME_FROM_SYSTEM_STATE structure](ns-pepfx--pep-ppm-resume-from-system-state.md) | Used by the PEP_NOTIFY_PPM_RESUME_FROM_SYSTEM_STATE notification that notifies the PEP that the system has just resumed from a system power state. |
| [PEP_PPM_TEST_IDLE_STATE structure](ns-pepfx--pep-ppm-test-idle-state.md) | The PEP_PPM_TEST_IDLE_STATE structure contains information about whether the processor can immediately enter a processor idle state. |
| [PEP_PREPARE_DEVICE structure](ns-pepfx--pep-prepare-device.md) | The PEP_PREPARE_DEVICE structure identifies a device that must be started up in preparation for its use by the operating system. |
| [PEP_PROCESSOR_FEEDBACK_COUNTER structure](ns-pepfx--pep-processor-feedback-counter.md) | The PEP_PROCESSOR_FEEDBACK_COUNTER structure describes a feedback counter to the operating system. |
| [PEP_PROCESSOR_IDLE_DEPENDENCY structure](ns-pepfx--pep-processor-idle-dependency.md) | The PEP_PROCESSOR_IDLE_DEPENDENCY structure specifies the dependencies of a platform idle state on the specified processor. |
| [PEP_PROCESSOR_IDLE_STATE_UPDATE structure](ns-pepfx--pep-processor-idle-state-update.md) | The PEP_PROCESSOR_IDLE_STATE_UPDATE structure contains the updated properties of a processor idle state. |
| [PEP_PROCESSOR_IDLE_STATE_V2 structure](ns-pepfx--pep-processor-idle-state-v2.md) | The PEP_PROCESSOR_IDLE_STATE_V2 structure describes a processor idle state that the platform extension plug-in (PEP) supports. |
| [PEP_PROCESSOR_PARK_PREFERENCE structure](ns-pepfx--pep-processor-park-preference.md) | The PEP_PROCESSOR_PARK_PREFERENCE structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding whether the specified processor should be parked to reduce power consumption. |
| [PEP_PROCESSOR_PARK_STATE structure](ns-pepfx--pep-processor-park-state.md) | The PEP_PROCESSOR_PARK_STATE structure describes the parking state for a single processor. |
| [PEP_PROCESSOR_PERF_STATE structure](ns-pepfx--pep-processor-perf-state.md) | Use in the PEP_NOTIFY_PPM_QUERY_DISCRETE_PERF_STATES  notification. This structure describes the properties of a single performance state.  . |
| [PEP_QUERY_COMPONENT_PERF_CAPABILITIES structure](ns-pepfx--pep-query-component-perf-capabilities.md) | The PEP_QUERY_COMPONENT_PERF_CAPABILITIES structure specifies the number of performance state (P-state) sets that are defined for a component. |
| [PEP_QUERY_COMPONENT_PERF_SET structure](ns-pepfx--pep-query-component-perf-set.md) | The PEP_QUERY_COMPONENT_PERF_SET structure contains query information about a set of performance state values (P-state set) for a component. |
| [PEP_QUERY_COMPONENT_PERF_SET_NAME structure](ns-pepfx--pep-query-component-perf-set-name.md) | The PEP_QUERY_COMPONENT_PERF_SET_NAME structure contains query information about a set of performance state values (P-state set) for a component. |
| [PEP_QUERY_COMPONENT_PERF_STATES structure](ns-pepfx--pep-query-component-perf-states.md) | The PEP_QUERY_COMPONENT_PERF_STATES structure contains a list of discrete performance state (P-state) values for the specified P-state set. |
| [PEP_QUERY_CURRENT_COMPONENT_PERF_STATE structure](ns-pepfx--pep-query-current-component-perf-state.md) | The PEP_QUERY_CURRENT_COMPONENT_PERF_STATE structure contains information about the current P-state in the specified P-state set. |
| [PEP_QUERY_SOC_SUBSYSTEM structure](ns-pepfx--pep-query-soc-subsystem.md) | The PEP_QUERY_SOC_SUBSYSTEM structure is used by the PEP_DPM_QUERY_SOC_SUBSYSTEM notification to gather basic information about a particular system on a chip (SoC) subsystem. |
| [PEP_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME structure](ns-pepfx--pep-query-soc-subsystem-blocking-time.md) | The PEP_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME structure is used by the PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME notification to collect details about the blocking duration for a particular system on a chip (SoC) subsystem. |
| [PEP_QUERY_SOC_SUBSYSTEM_COUNT structure](ns-pepfx--pep-query-soc-subsystem-count.md) | The PEP_QUERY_SOC_SUBSYSTEM_COUNT structure is used to tell the OS whether the PEP supports system on a chip (SoC) subsystem accounting for a given platform idle state. |
| [PEP_QUERY_SOC_SUBSYSTEM_METADATA structure](ns-pepfx--pep-query-soc-subsystem-metadata.md) | The PEP_QUERY_SOC_SUBSYSTEM_METADATA structure is used with the PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA notification to collect optional metadata about the system on a chip (SoC) subsystem whose blocking time has just been queried. |
| [PEP_REGISTER_COMPONENT_PERF_STATES structure](ns-pepfx--pep-register-component-perf-states.md) | The PEP_REGISTER_COMPONENT_PERF_STATES structure describes the performance states (P-states) of the specified component. |
| [PEP_REGISTER_CRASHDUMP_DEVICE structure](ns-pepfx--pep-register-crashdump-device.md) | The PEP_REGISTER_CRASHDUMP_DEVICE structure provides a callback routine to turn on a crash-dump device. |
| [PEP_REGISTER_DEBUGGER structure](ns-pepfx--pep-register-debugger.md) | The PEP_REGISTER_DEBUGGER structure identifies a registered device that is a core system resource that provides debugger transport. |
| [PEP_REGISTER_DEVICE_V2 structure](ns-pepfx--pep-register-device-v2.md) | The PEP_REGISTER_DEVICE_V2 structure describes a device whose driver stack has just registered with the Windows power management framework (PoFx). |
| [PEP_REQUEST_COMPONENT_PERF_STATE structure](ns-pepfx--pep-request-component-perf-state.md) | The PEP_REQUEST_COMPONENT_PERF_STATE structure contains a list of performance state (P-state) changes requested by the Windows power management framework (PoFx), plus status information about the handling of these requests by the platform extension plug-in (PEP). |
| [PEP_RESET_SOC_SUBSYSTEM_ACCOUNTING structure](ns-pepfx--pep-reset-soc-subsystem-accounting.md) | The PEP_RESET_SOC_SUBSYSTEM_ACCOUNTING structure is provided to the platform extension plug-in (PEP) as part of a PEP_DPM_RESET_SOC_SUBSYSTEM_ACCOUNTING notification. |
| [PEP_SOC_SUBSYSTEM_METADATA structure](ns-pepfx--pep-soc-subsystem-metadata.md) | The PEP_SOC_SUBSYSTEM_METADATA structure contains key-value pairs that contain metadata for a system on a chip (SoC) subsystem. It is used in the context of a PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA notification sent to a platform extension plug-in (PEP). |
| [PEP_SYSTEM_LATENCY structure](ns-pepfx--pep-system-latency.md) | The PEP_SYSTEM_LATENCY structure specifies the new value for the system latency tolerance. |
| [PEP_UNMASKED_INTERRUPT_FLAGS structure](ns-pepfx--pep-unmasked-interrupt-flags.md) | The PEP_UNMASKED_INTERRUPT_FLAGS union indicates whether an unmasked interrupt source is a primary interrupt or a secondary interrupt. |
| [PEP_UNMASKED_INTERRUPT_INFORMATION structure](ns-pepfx--pep-unmasked-interrupt-information.md) | The PEP_UNMASKED_INTERRUPT_INFORMATION structure contains information about an interrupt source. |
| [PEP_UNREGISTER_DEVICE structure](ns-pepfx--pep-unregister-device.md) | The PEP_UNREGISTER_DEVICE structure identifies a device whose registration is being removed from the Windows power management framework (PoFx). |
| [PEP_WORK structure](ns-pepfx--pep-work.md) | The PEP_WORK structure indicates whether the PEP has a work request to submit to the Windows power management framework (PoFx). |
| [PEP_WORK_ACPI_EVALUATE_CONTROL_METHOD_COMPLETE structure](ns-pepfx--pep-work-acpi-evaluate-control-method-complete.md) | The PEP_WORK_ACPI_EVALUATE_CONTROL_METHOD_COMPLETE structure contains the results of an ACPI control method that was asynchronously evaluated by the platform extension plug-in (PEP). |
| [PEP_WORK_ACPI_NOTIFY structure](ns-pepfx--pep-work-acpi-notify.md) | The PEP_WORK_ACPI_NOTIFY structure contains the ACPI Notify code for a device that has generated a hardware event. |
| [PEP_WORK_COMPLETE_IDLE_STATE structure](ns-pepfx--pep-work-complete-idle-state.md) | The PEP_WORK_COMPLETE_IDLE_STATE structure identifies a component that the platform extension plug-in (PEP) has prepared for a transition to a new Fx power state. |
| [PEP_WORK_COMPLETE_PERF_STATE structure](ns-pepfx--pep-work-complete-perf-state.md) | The PEP_WORK_COMPLETE_PERF_STATE structure describes the completion status of a previously requested update to the performance values assigned to a list of performance state (P-state) sets. |
| [PEP_WORK_INFORMATION structure](ns-pepfx--pep-work-information.md) | The PEP_WORK_INFORMATION structure describes a work item that the PEP is submitting to the Windows power management framework (PoFx). |
| [PEP_WORK_POWER_CONTROL structure](ns-pepfx--pep-work-power-control.md) | The PEP_WORK_POWER_CONTROL structure contains the parameters for a power control request that the platform extension plug-in (PEP) sends directly to a processor driver. |
| [PO_FX_CORE_DEVICE structure](ns-pepfx--po-fx-core-device.md) | The PO_FX_CORE_DEVICE structure contains information about the power-state attributes of the components in a core system resource, and provides a software interface for power-managing these components. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [GPIO_PIN_CONFIG_TYPE enumeration](ne-pepfx--gpio-pin-config-type.md) | The GPIO_PIN_CONFIG_TYPE enumeration describes a connection IO resource. |
| [GPIO_PIN_IORESTRICTION_TYPE enumeration](ne-pepfx--gpio-pin-iorestriction-type.md) | The GPIO_PIN_IORESTRICTION_TYPE enumeration describes the functions that a GPIO pin is limited to performing. |
| [PEP_ACPI_OBJECT_TYPE enumeration](ne-pepfx--pep-acpi-object-type.md) | The PEP_ACPI_OBJECT_TYPE enumeration indicates the type of ACPI object. |
| [PEP_ACPI_RESOURCE_TYPE enumeration](ne-pepfx--pep-acpi-resource-type.md) | The PEP_ACPI_RESOURCE_TYPE enumeration is used to identify the type of ACPI resource that is contained in the PEP_ACPI_RESOURCE union. |
| [PEP_DEVICE_ACCEPTANCE_TYPE enumeration](ne-pepfx--pep-device-acceptance-type.md) | The PEP_DEVICE_ACCEPTANCE_TYPE enumeration indicates whether a PEP accepts ownership of a device. |
| [PEP_PERF_STATE_TYPE enumeration](ne-pepfx--pep-perf-state-type.md) | The PEP_PERF_STATE_TYPE enumeration indicates the type of performance information that is specified for a performance state (P-state) of a component. |
| [PEP_PERF_STATE_UNIT enumeration](ne-pepfx--pep-perf-state-unit.md) | The PEP_PERF_STATE_UNIT enumeration indicates the measurement units in which the performance state (P-state) of a component is specified. |
| [PEP_WORK_TYPE enumeration](ne-pepfx--pep-work-type.md) | The PEP_WORK_TYPE enumeration describes the type of work that the platform extension plug-in (PEP) is requesting. |
